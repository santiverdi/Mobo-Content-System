# CLAUDE.md — MOBO Content System

## Qué es este repo

Sistema de contenido para MOBO (@mobomdp), tienda de hardware en Mar del
Plata. Contiene un system prompt + 8 archivos de knowledge que se cargan
manualmente al Project de claude.ai correspondiente.

El dueño de la marca y creador de contenido es Santi. Habla rioplatense
argentino, voseo, registro informal. NUNCA español neutro, NUNCA
mexicanismos.

## Cómo está organizado

- `00_SYSTEM_PROMPT.md` → instrucciones del Project (NO knowledge file)
- `01_BRAND_MOBO.md` → identidad, audiencia, tono, prohibiciones
- `02_FORMATO_A_HABLANDO_A_CAMARA.md` → desmitificador, sin CTAs
- `03_FORMATO_B_PRINCI_VS_PRO.md` → diálogo con bardeo y plug embebido
- `04_FORMATO_C_DEADPAN_PAYEROS.md` → compilado de arquetipos
- `05_FORMATO_D_STORIES.md` → Stories selfie + venta directa
- `06_REFERENTES_Y_AUDIT.md` → AUTORIDAD MÁXIMA. Métricas reales > opiniones.
- `07_IDEAS_POOL.md` → banco de 214 ideas + ejecutadas + pendientes
- `08_GUIONES_VIRALES_LITERAL.md` → transcripciones literales de virales
- `09_NEUROCIENCIA.md` → consulta OPTATIVA cuando un hook pasa el filtro pero no convence. Nunca sustituye al audit (06).
- `10_FORMATO_E_PREGUNTA_DEL_FONDO.md` → Q&A off-cam con opinión filosa, protocolo de mitigación obligatorio si afecta MOBO
- `_exports_originales/` → backups, no editar
- `_archivos_originales_de_projects/` → archivos crudos, no editar
- `_scripts/` → scripts de scraping y análisis. `mobo_comments.csv` (18K comments YT) + `mobo_comments_report.md` (análisis temático). Reproducible. Ver Audit de comentarios en `06_REFERENTES_Y_AUDIT.md`.

## Reglas operativas para Claude Code

### Cuando edites archivos del sistema:

1. **NUNCA inventes specs, precios o benchmarks.** Si no tenés el dato
   verificable, dejá un comentario `<!-- VERIFICAR: [qué falta] -->` y
   avisame.

2. **Mantenete dentro del rioplatense.** Si encontrás algún "tú", "vosotros",
   "checa", "qué onda", "ordenador", "vídeo", "móvil", "computadora"
   (decimos PC) → corregilo. Reportame si lo encontraste.

3. **El audit (`06_REFERENTES_Y_AUDIT.md`) es ley.** Si una decisión nueva
   contradice algo del audit, parar y preguntarme antes de aplicar.

4. **Duración máxima de cualquier guion: 47 segundos.** Si te pido un
   guion más largo, recordame esta regla antes de escribir.

5. **No mezcles formatos.** Cada formato tiene su archivo. Si pido un
   guion y el tema podría ir en dos formatos, preguntame cuál antes
   de escribir.

6. ### Cuando un hook pasa el filtro pero no convence:

   Consultar `09_NEUROCIENCIA.md` para diagnosticar. Las dos secciones
   útiles son:

   - **Curiosity Gap**: tres preguntas para chequear si el gap está bien
     formulado (awareness previa del viewer / gap delimitado / resoluble
     en 30-45s).
   - **Identificación social**: cuatro preguntas para chequear primera
     persona, presente, emoción activa, situación específica.

   Si el hook falla en estos diagnósticos, proponer reformulación
   basada en el mecanismo que falle. Si una recomendación de neurociencia
   contradice el audit (06), gana el audit.

### Workflow específico de Formato B (PRINCI vs PRO):

Validado empíricamente que los guiones 100% Claude rinden peor que los
autoescritos por Santi. Cuando te pida un guion B, entregá los **pilares
estructurales**, no el diálogo final:

1. Lo que cree el principiante (conclusión equivocada con acción inminente)
2. Problema real
3. Pregunta que lo delata
4. Info técnica que tiene que quedar
5. Solución concreta
6. Detalle secundario opcional (false lead / digresión absurda)

Avisá al final que la versión final tiene que pasar por la pluma de Santi.

### Cuando agregue ideas o cierre videos:

- Idea ejecutada → marcar con ✅ en `07_IDEAS_POOL.md`
- Idea descartada → mover a una sección "Descartadas" con razón breve
- Nueva métrica de un video publicado → agregar a `06_REFERENTES_Y_AUDIT.md`
- Guion validado por números (>50K views o >2% share rate) → transcribir
  literal en `08_GUIONES_VIRALES_LITERAL.md`

### Lenguaje prohibido (NUNCA generar):

- "Es como tener una Ferrari y andar en colectivo"
- "Ferrari/Fitito" en cualquier variación
- "Cebarme un mate mientras..."
- "Un cable es un cable"
- Reciclar la misma analogía entre guiones distintos
- CTAs genéricos ("seguime", "dale like", "guardá este video")
- "Comentá tu [procesador/placa/RAM/lo que sea] y seguime para más videos" (CTA prohibido literal, validado flop mayo 2026)

### Anti-patrón obligatorio: "spoiler en el hook"

Antes de validar cualquier hook, leerlo en voz alta. Si la frase de apertura
contiene tanto la creencia común como la revelación que la rompe, el gap
muere y el video flopea (validado con incognito myth, mayo 2026: 1.4K views
en 1h con tema universal). Ver Regla 10 en `06_REFERENTES_Y_AUDIT.md`.
El hook plantea el setup o la pregunta, nunca la revelación.

### Test de filtro para cualquier idea nueva:

Antes de desarrollar, contestá:
1. ¿El conflicto es del viewer o del creador? (tiene que ser del viewer)
2. ¿Tiene un twist o es lineal? (tutorial lineal = saves, no shares)
3. ¿Alguien lo mandaría por WhatsApp o solo lo guardaría?
4. ¿El hook nombra un modelo exacto (Ryzen 7 5700X) o una familia genérica (Ryzen 5)? Si es familia → reformular con modelo exacto. Ver Regla 11 en `06_REFERENTES_Y_AUDIT.md`.
5. ¿Hay un **personaje real** (cliente del local, viewer arquetipo, hermano) o es recomendación neutral? Sin personaje, el video tiene techo bajo en MOBO (Regla 20 del audit, validada con corpus de 18K comments).

Si las cinco no son favorables, no escribir el guion. Avisar y reformular.

## Sobre git

- Cuando termines una sesión productiva, sugerime un commit message
  conciso (50 chars) que resuma los cambios.
- Si edité archivos críticos (00, 01, 06), recordame que hay que
  re-subirlos al Project de claude.ai porque Claude no los lee desde
  el repo automáticamente.
- Cuando estés por hacer cambios grandes, sugerí crear una rama nueva
  antes (ej: `experimentos/nuevo-formato`).

## Sobre el estilo de respuesta conmigo

- Argentino, peer, no profesor.
- Brutalmente honesto. Si una idea es flojo, decímelo.
- No me asumas correcto sin verificar.
- Cerrá con próximo paso accionable.
- Sin emojis salvo que yo los use primero.
