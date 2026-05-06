"""Analyze MOBO YouTube comments: pains, debates, questions, objections."""
import csv
import io
import re
import sys
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CSV_PATH = "mobo_comments.csv"
OUT_PATH = "mobo_comments_report.md"

# Topic clusters with keyword regexes (lowercase match)
TOPICS = {
    "Cuello de botella CPU/GPU": [r"cuello de botella", r"bottleneck", r"botella"],
    "Ryzen 5 (genérico)": [r"\bryzen 5\b(?! \d)", r"\br5\b(?! \d)"],
    "Ryzen 5 5600 / 5600X / 5600G": [r"5600x?\b", r"5600g\b"],
    "Ryzen 7 5700X / 5800X": [r"5700x\b", r"5800x\b", r"\bryzen 7\b"],
    "Ryzen 9 / 7700X / 7800X3D": [r"7700x\b", r"7800x3d\b", r"ryzen 9"],
    "Intel i3 / i5 / i7 / i9": [r"\bi[3579]\b[\s-]?\d", r"intel"],
    "RTX 3060 / 3060 Ti": [r"3060\s?ti\b", r"\b3060\b"],
    "RTX 4060 / 4070": [r"4060\s?ti\b", r"\b4060\b", r"\b4070\b"],
    "RTX 5090 / 5080 / 5070": [r"5090\b", r"5080\b", r"5070\b"],
    "GTX 1650 / 1660": [r"1650\b", r"1660\b"],
    "RX 6600 / 6700 / 6800": [r"\b6600\b", r"6700\s?xt\b", r"\b6800\b"],
    "DLSS / FSR": [r"dlss", r"\bfsr\b"],
    "RAM (canales / dual)": [r"\bram\b", r"dual channel", r"memoria", r"\bddr[345]\b"],
    "RAM 1x16 vs 2x8 (debate específico)": [r"1\s?x\s?16", r"2\s?x\s?8", r"un palo de 16", r"dos de 8", r"una de 16"],
    "Motherboard / VRM / Chipset": [r"\bmother", r"\bvrm\b", r"a320", r"b450", r"b550", r"b650", r"x570", r"placa madre", r"motherboard"],
    "Fuente / PSU": [r"fuente", r"\bpsu\b", r"\bwatt", r"\bw\b\s*(de|fuente)", r"80\s?plus"],
    "Almacenamiento SSD/M.2/NVMe": [r"\bssd\b", r"\bm\.?2\b", r"\bnvme\b", r"sata", r"hdd", r"disco"],
    "Refrigeración / temperaturas": [r"temperatu", r"\b\d{2,3}\s?grados", r"watercool", r"liquid", r"airflow", r"flujo de aire", r"cooler", r"ventila"],
    "FPS / rendimiento": [r"\bfps\b", r"frames", r"rendimiento", r"performance"],
    "Compatibilidad / actualizar": [r"compatib", r"actualiza[rd]", r"upgrade", r"sirve para", r"anda con", r"funciona con"],
    "Comprar usado / mercadolibre": [r"\busado\b", r"mercado libre", r"mercadolibre", r"\bml\b"],
    "Precio / es caro / pesos / dolares": [r"caro", r"barato", r"\bplata\b", r"\bguita\b", r"precio", r"sale\s+\d", r"cuesta"],
    "Consola vs PC": [r"consola", r"\bps[345]\b", r"playstation", r"xbox"],
    "Notebook / laptop": [r"notebook", r"laptop", r"\bnoteb"],
    "Streaming / fortnite / valorant / cs": [r"stream", r"fortnite", r"valorant", r"\bcs\s?(go|2)?\b", r"twitch"],
    "Windows / activador / actualizacion": [r"windows", r"\bw11\b", r"\bw10\b", r"activador"],
    "Gabinete / aireación / RGB": [r"gabinete", r"\brgb\b", r"\bcase\b"],
    "Monitor / hz / resolución": [r"monitor", r"\bhz\b", r"\b144\s?hz", r"\b1080p\b", r"\b1440p\b", r"\b4k\b", r"vsync"],
}

# Buying objection signals
OBJECTIONS = {
    "Es caro / no me alcanza": [r"caro", r"no me alcanza", r"no llego", r"está cara", r"esta cara", r"sale un palo"],
    "Mejor compro consola": [r"mejor.*consola", r"me paso a (la )?(ps|consola)", r"vendo la pc"],
    "Mejor compro usado": [r"prefiero usado", r"mejor usado", r"compro usado", r"de segunda"],
    "Desconfianza envío / online": [r"envío", r"envio", r"llega bien", r"confiar", r"se rompe"],
    "Ya tengo X (defensivo)": [r"yo tengo", r"yo uso", r"a mi me anda", r"el mio anda"],
    "Estafa / engaño": [r"estafa", r"chamuyo", r"verso", r"mentira"],
}

QUESTION_WORDS = ["?", "¿", "como", "cómo", "que", "qué", "cual", "cuál", "porque",
                  "por qué", "sirve", "anda", "vale la pena", "conviene", "mejor"]

def lower(s):
    return s.lower() if s else ""

# Load comments
rows = []
with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        try:
            r["likes"] = int(r["likes"] or 0)
        except ValueError:
            r["likes"] = 0
        r["text_lc"] = lower(r["text"])
        r["len"] = len(r["text"])
        rows.append(r)

print(f"Total comments cargados: {len(rows)}")

# Filter signal
signal = [r for r in rows if r["len"] >= 30 or r["likes"] >= 1 or "?" in r["text"]]
print(f"Comments con señal (>=30 chars, likes>=1, o pregunta): {len(signal)}")

# Topic counts + examples
topic_hits = defaultdict(list)
for r in signal:
    for topic, patterns in TOPICS.items():
        for p in patterns:
            if re.search(p, r["text_lc"]):
                topic_hits[topic].append(r)
                break

# Objections
obj_hits = defaultdict(list)
for r in signal:
    for obj, patterns in OBJECTIONS.items():
        for p in patterns:
            if re.search(p, r["text_lc"]):
                obj_hits[obj].append(r)
                break

# Questions: comments that contain "?" AND a question word, len 30-300
questions = [r for r in signal if "?" in r["text"] and 25 <= r["len"] <= 300]
# Sort by likes desc
questions.sort(key=lambda r: r["likes"], reverse=True)

# Top liked comments overall (validated reactions)
top_liked = sorted(rows, key=lambda r: r["likes"], reverse=True)[:30]

# Build report
out = []
out.append("# MOBO Comments Report — análisis de 18,424 comentarios\n")
out.append(f"Fuente: `mobo_comments.csv` · Canal: Muun Tech · 309 videos\n")
out.append(f"Comments con señal analizados: **{len(signal)}**\n\n---\n")

out.append("## TOP 20 — Temas más mencionados\n")
ranked = sorted(topic_hits.items(), key=lambda x: -len(x[1]))[:20]
for topic, hits in ranked:
    out.append(f"### {topic} — {len(hits)} menciones\n")
    # Top 3 by likes for examples
    examples = sorted(hits, key=lambda r: r["likes"], reverse=True)[:3]
    for e in examples:
        text = e["text"][:200].replace("\n", " ")
        out.append(f"- *\"{text}\"* — **{e['likes']} likes** · video: *{e['video_title'][:60]}*\n")
    out.append("\n")

out.append("\n---\n## OBJECIONES DE COMPRA detectadas\n")
for obj, hits in sorted(obj_hits.items(), key=lambda x: -len(x[1])):
    if not hits:
        continue
    out.append(f"### {obj} — {len(hits)} menciones\n")
    examples = sorted(hits, key=lambda r: r["likes"], reverse=True)[:2]
    for e in examples:
        text = e["text"][:200].replace("\n", " ")
        out.append(f"- *\"{text}\"* — {e['likes']} likes · *{e['video_title'][:50]}*\n")
    out.append("\n")

out.append("\n---\n## TOP 30 PREGUNTAS REPETIDAS (ordenadas por likes)\n")
out.append("Cada una es un dolor real con conflicto del viewer.\n\n")
for q in questions[:30]:
    text = q["text"][:250].replace("\n", " ")
    out.append(f"- *\"{text}\"* — **{q['likes']} likes** · *{q['video_title'][:55]}*\n")

out.append("\n---\n## TOP 30 COMENTS MÁS LIKEADOS (validación social pura)\n")
out.append("Los comments con más likes muestran qué resuena. Útil para detectar arquetipos.\n\n")
for r in top_liked:
    text = r["text"][:200].replace("\n", " ")
    out.append(f"- *\"{text}\"* — **{r['likes']} likes** · *{r['video_title'][:55]}*\n")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print(f"\nLISTO: reporte en {OUT_PATH}")
print(f"Top 5 temas:")
for topic, hits in ranked[:5]:
    print(f"  {topic}: {len(hits)}")
