# MOBO Content System — v2 (consolidado)

Sistema fusionado a partir de 4 Projects de Claude. Decisiones editoriales tomadas por Santi:

- **Filosofía editorial:** mezcla — desmitificador en hablando-a-cámara, bardeo + plug en PRINCI vs PRO.
- **Duración máxima:** 47 segundos para todo formato (regla del audit empírico).
- **Audit empírico es ley:** cuando los Projects se contradigan, gana lo que dice el audit con métricas reales.

---

## Cómo se usa

### 1. System prompt
Pegá `00_SYSTEM_PROMPT.md` en el campo "Instructions" del Project nuevo.

### 2. Knowledge files (subir al Project)
- `01_BRAND_MOBO.md` — identidad, audiencia, tono, prohibiciones
- `02_FORMATO_A_HABLANDO_A_CAMARA.md` — desmitificador, 4 bloques, modos
- `03_FORMATO_B_PRINCI_VS_PRO.md` — diálogo, conclusión equivocada, bardeo
- `04_FORMATO_C_DEADPAN_PAYEROS.md` — compilado de arquetipos
- `05_FORMATO_D_STORIES.md` — selfie + venta directa, 4-5 stories/día
- `06_REFERENTES_Y_AUDIT.md` — Payeros, MetaPCs, métricas reales, fórmula ganadora
- `07_IDEAS_POOL.md` — banco de 214 ideas + ejecutadas + pendientes
- `08_GUIONES_VIRALES_LITERAL.md` — transcripciones literales de los videos que rindieron
- `09_NEUROCIENCIA.md` — mecanismos neurocientíficos optativos (Curiosity Gap, Identificación social)
- `10_FORMATO_E_PREGUNTA_DEL_FONDO.md` — Q&A off-cam con opinión filosa

### 3. Mantenimiento
Cuando termines una sesión productiva:
- Nueva idea ejecutada → marcar en `07_IDEAS_POOL.md`
- Nuevo aprendizaje empírico (post métricas) → agregar a `06_REFERENTES_Y_AUDIT.md`
- Guion validado por números → transcribirlo en `08_GUIONES_VIRALES_LITERAL.md`

---

## Cambios respecto a la v1 (la que armamos al principio)

1. **Más archivos.** v1 tenía 4 archivos cortos. v2 tiene 8 más densos con material literal preservado.
2. **Cada formato tiene su propio archivo.** Antes estaban todos en uno solo.
3. **Audit empírico separado** del archivo de referentes — porque tiene autoridad máxima y conviene que esté en su propio espacio.
4. **Transcripciones literales** de los videos virales como archivo aparte. Esto es lo más valioso: calibra la voz de Santi a Claude mejor que cualquier descripción.
5. **Banco de 214 ideas categorizadas** de un Project que tenía esto trabajado.

---

## Lo que descarté de los exports (a propósito)

De los 4 exports llegaron cosas que NO van en este sistema:

- **MetaPCs guiones literales (en inglés):** los análisis estructurales sí, los transcripts en inglés no. Si los necesitás, están en el archivo original `metapcs-guiones-con-analisis.md`.
- **Workflow de Gemini para research:** es operativo, no creativo. Si volvés a usarlo, mantenelo en otro lado.
- **Sub-arcos técnicos** (Whisper que no funcionó, scrapers, MCPs): ruido para este Project.
- **Hotel Dion:** otra marca, otro Project.
- **Memorias internas en inglés:** las traduje al castellano y las integré donde corresponde.

---

## Gaps que NO se resolvieron (a tener en cuenta)

1. **Catálogo de productos / precios MOBO:** ningún Project lo tiene formalizado. Si querés que Claude te ayude con copies de venta, vas a tener que sumar un archivo `09_CATALOGO_MOBO.md` a mano.
2. **Métricas históricas más allá del audit:** el audit cubre Mar 8 – Abr 4. No hay datos más viejos ni más nuevos.
3. **Project paralelo de simulador de viewer:** existe pero no fue exportado. Si lo querés integrar, hay que vaciarlo aparte.
4. **Pipeline de Claude Code (`/mobo-guion`, `/mobo-audit`):** vive afuera de este Project. No lo toco.
5. **Build presentations:** mencionado en uno de los Projects pero sin framework. Cuando lo armes, va a un archivo nuevo.
