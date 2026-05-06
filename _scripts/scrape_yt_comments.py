"""Scrape all comments from MOBO YouTube channel into CSV."""
import csv
import io
import json
import sys
import time
import urllib.parse
import urllib.request

# Force UTF-8 stdout so emojis in titles don't crash prints
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

API_KEY = sys.argv[1]
HANDLE = "muuntechh"
OUT_CSV = sys.argv[2] if len(sys.argv) > 2 else "mobo_comments.csv"
BASE = "https://www.googleapis.com/youtube/v3"


def get(url):
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())


def api(endpoint, **params):
    params["key"] = API_KEY
    qs = urllib.parse.urlencode(params)
    return get(f"{BASE}/{endpoint}?{qs}")


# 1. Resolve handle -> channel ID -> uploads playlist
ch = api("channels", part="contentDetails,snippet,statistics", forHandle=HANDLE)
if not ch.get("items"):
    print(f"Canal no encontrado: @{HANDLE}", file=sys.stderr)
    sys.exit(1)
channel = ch["items"][0]
uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
print(f"Canal: {channel['snippet']['title']}  videos: {channel['statistics'].get('videoCount')}")

# 2. List all videos
videos = []
page = None
while True:
    params = dict(part="snippet,contentDetails", playlistId=uploads, maxResults=50)
    if page:
        params["pageToken"] = page
    r = api("playlistItems", **params)
    for it in r["items"]:
        videos.append({
            "video_id": it["contentDetails"]["videoId"],
            "title": it["snippet"]["title"],
            "published": it["contentDetails"].get("videoPublishedAt", ""),
        })
    page = r.get("nextPageToken")
    if not page:
        break
print(f"Videos encontrados: {len(videos)}")

# 3. Fetch comments per video
rows = []
for i, v in enumerate(videos, 1):
    print(f"[{i}/{len(videos)}] {v['title'][:60]}", flush=True)
    page = None
    fetched = 0
    while True:
        try:
            params = dict(
                part="snippet,replies",
                videoId=v["video_id"],
                maxResults=100,
                textFormat="plainText",
                order="relevance",
            )
            if page:
                params["pageToken"] = page
            r = api("commentThreads", **params)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            if "commentsDisabled" in body or e.code == 403:
                print(f"  comments disabled / forbidden: {e.code}")
                break
            print(f"  error {e.code}: {body[:200]}")
            break
        for thread in r.get("items", []):
            top = thread["snippet"]["topLevelComment"]["snippet"]
            rows.append({
                "video_id": v["video_id"],
                "video_title": v["title"],
                "video_published": v["published"],
                "comment_id": thread["snippet"]["topLevelComment"]["id"],
                "parent_id": "",
                "author": top.get("authorDisplayName", ""),
                "text": top.get("textDisplay", "").replace("\n", " "),
                "likes": top.get("likeCount", 0),
                "published_at": top.get("publishedAt", ""),
            })
            fetched += 1
            for rep in thread.get("replies", {}).get("comments", []):
                s = rep["snippet"]
                rows.append({
                    "video_id": v["video_id"],
                    "video_title": v["title"],
                    "video_published": v["published"],
                    "comment_id": rep["id"],
                    "parent_id": thread["snippet"]["topLevelComment"]["id"],
                    "author": s.get("authorDisplayName", ""),
                    "text": s.get("textDisplay", "").replace("\n", " "),
                    "likes": s.get("likeCount", 0),
                    "published_at": s.get("publishedAt", ""),
                })
                fetched += 1
        page = r.get("nextPageToken")
        if not page:
            break
    print(f"  comments: {fetched}")

# 4. Write CSV
with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=[
        "video_id", "video_title", "video_published",
        "comment_id", "parent_id", "author", "text", "likes", "published_at",
    ])
    w.writeheader()
    w.writerows(rows)
print(f"\nLISTO: {len(rows)} comments -> {OUT_CSV}")
