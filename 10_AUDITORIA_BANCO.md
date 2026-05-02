# Auditoría del banco de ideas — 2026-05-02

## Resumen ejecutivo

- Total ideas procesadas: 214
- 🟢 Alto potencial: 51 (A1:22 + A2:14 + A3:7 + A4:8 + A5:0)
- 🟡 Reformulación: 58 (A1:18 + A2:14 + A3:8 + A4:14 + A5:4)
- 🟠 Dudoso: 28 (A1:11 + A2:10 + A3:4 + A4:10 + A5:3)
- 🔴 Descartar: 77 (A1:9 + A2:12 + A3:26 + A4:6 + A5:14)

> **Nota sobre calibración de agentes**: el Agente 3 (Datos curiosos + Tips) fue notablemente más estricto que los demás, con 26 descartadas de 45 ideas procesadas (58% de tasa de descarte vs 15-22% del resto). Esta diferencia no es un error — el bloque de datos curiosos tiene el mayor porcentaje de trivia pura del banco y el Agente 3 aplicó el criterio del audit con rigor total, citando evidencia empírica directa (PS3 supercomputadora 3/10, Tip para limpiar PC 2/10). La clasificación es correcta. Por el contrario, el Agente 4 (Storytime) fue el más permisivo en 🟡: muchas ideas que tienen causa oculta fuerte quedaron en reformulable por el problema de hook en tercera persona — eso es reformulación menor, no descarte.

> El Agente 5 (Tutoriales + Versus) es el único con 0 ideas en 🟢, lo cual refleja la calidad del bloque, no la dureza del criterio. Los tutoriales formulados como "cómo hacer X paso a paso" son estructuralmente incompatibles con el formato viral de ≤47 segundos.

Adaptabilidad a Formato A:
- ⭐ A-Nativas: 55 (A1:14 + A2:22 + A3:10 + A4:7 + A5:2)
- 🔄 A-Adaptables: 94 (A1:28 + A2:18 + A3:6 + A4:22 + A5:5)
- ❌ A-Incompatibles: 65 (A1:18 + A2:10 + A3:3 + A4:9 + A5:14)

**CRUCE 🟢 + ⭐ (oro inmediato): 22 ideas**

---

## TOP 10 PARA GRABAR ESTA SEMANA EN FORMATO A

**Criterio**: las 10 que combinan 🟢 + ⭐ (o 🟢 + 🔄 donde la adaptación es trivial), priorizando Curiosity Gap más fuerte y datos ancla disponibles.

---

**#1 — A1 idea 038 | "Tengo FPS altos pero el juego se siente raro"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Tengo 120 FPS y el juego se siente como si fueran 30. Y no sé por qué."*
- Dato ancla: VSync activado = input lag, Hz del monitor como techo real, 1% lows como métrica oculta. Dato verificable con cualquier herramienta de overlay.
- Por qué entró: curiosity gap perfecto — el viewer tiene los números, tiene la sensación y no entiende la contradicción. WhatsApp-able máximo.

---

**#2 — A2 Mitos 011 | "Todos los cables USB-C son iguales"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Conecté mi notebook con el cable del celular y no carga. El cable de al lado sí. Son iguales visualmente."*
- Dato ancla: diferencia USB 2.0 / USB 3.2 / Thunderbolt / USB4 en un mismo form factor — verificable en cualquier caja de cable o spec sheet.
- Por qué entró: creencia universal activa + consecuencia inmediata + el viewer tiene 5 cables USB-C mezclados en el cajón ahora mismo.

---

**#3 — A2 Mitos 004 | "El modo incógnito te hace invisible en internet"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Uso el modo incógnito desde siempre pensando que nadie me ve. Me acabo de enterar que el ISP ve todo igual."*
- Dato ancla: qué esconde y qué no esconde el modo incógnito — dato documentado en la propia página de ayuda de Chrome/Firefox.
- Por qué entró: creencia activa en el 90% de la audiencia + twist con consecuencia práctica real + WhatsApp-able masivo.

---

**#4 — A2 Mitos 007 | "Tenés que desfragmentar tu SSD"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Desfragmenté el SSD porque me dijeron que era necesario. Acabo de enterarme de que lo estaba dañando."*
- Dato ancla: ciclos de escritura de NAND flash, TRIM vs defrag — documentado por fabricantes (Samsung, Crucial). Dato verificable y específico.
- Por qué entró: creencia heredada del HDD muy activa + consecuencia real sobre vida útil del hardware + twist limpio.

---

**#5 — A2 Directo 009 | "Tu ISP te está cagando y no te das cuenta"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Pago 600 megas de internet. Hice el test y me da 600. Me estaban cagando igual."*
- Dato ancla: diferencia entre velocidad en speedtest (con protocolo favorable) y velocidad real de descarga en picos de demanda — el mismo patrón que el viral de bits vs bytes (hook 8/10 en audit). VERIFICAR: dato local de ISP en Mar del Plata para anclar.
- Por qué entró: injusticia económica activa + mismo esquema que el viral de 1 Gbps ≠ 100 MB/s validado en el audit.

---

**#6 — A2 Mitos 003 | "Necesitás un antivirus pago en 2025"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Pago $X por mes de antivirus. Me acabo de dar cuenta de que Windows ya tiene uno gratis que es igual de bueno."*
- Dato ancla: AV-TEST comparativa Defender vs Kaspersky/ESET 2024-2025 — dato verificable, publicado regularmente. VERIFICAR: precio en pesos de las licencias más comunes en Argentina.
- Por qué entró: gasto recurrente evitable + twist que beneficia económicamente al viewer + altamente WhatsApp-able.

---

**#7 — A4 Storytime ensamble 004 | "Upgradear vs armar de cero: qué convenía"**
- Modo Formato A: Anécdota
- Hook tentativo: *"Iba a upgradear la GPU. El técnico me dijo que me convenía armar de cero. Hice los números y casi me cago de risa."*
- Dato ancla: costo de upgrade parcial vs plataforma nueva — necesita números reales de un caso concreto reciente. VERIFICAR: ejemplo con precios de mercado argentino actuales.
- Por qué entró: decisión que enfrenta el 80% de los viewers con PC de más de 4 años + curiosity gap del resultado + WhatsApp-able porque el viewer lo manda a quien está en la misma situación.

---

**#8 — A3 Datos 024 | "JPG destruye tu imagen cada vez que la guardás"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Edité la foto, la guardé como JPG, la volví a abrir, la corregí un poco y la guardé de nuevo. La estaba destruyendo sin saberlo."*
- Dato ancla: compresión lossy acumulativa del formato JPG — dato técnico verificable, demostrable visualmente con comparación de generaciones de guardado.
- Por qué entró: el viewer hace esto todos los días + causa oculta + consecuencia concreta y visible + WhatsApp-able.

---

**#9 — A2 Directo 005 | "No existe la PC future-proof"**
- Modo Formato A: Explicativo
- Hook tentativo: *"Me gasté el doble para no tener que gastar en 2 años. Dos años después, igual tengo que gastar."*
- Dato ancla: ciclos históricos de obsolescencia de GPU/CPU — dato verificable con lanzamientos de Nvidia/AMD de los últimos 4 años.
- Por qué entró: creencia activa que mueve decisiones de compra de miles de pesos + twist que libera al viewer de una ilusión costosa + WhatsApp-able entre los que están convenciendo a alguien de gastar más.

---

**#10 — A4 Storytime ensamble 001 | "PC gamer de 500 USD para un pibe de 15"**
- Modo Formato A: Storytelling
- Hook tentativo: *"Tengo 500 dólares, mi viejo no sabe nada de PC y me tiene que armar la primera build. Lo que pasó después."*
- Dato ancla: builds reales posibles en presupuesto limitado en Argentina 2026 — VERIFICAR: precios actualizados de componentes en mercado local.
- Por qué entró: conflicto universal (presupuesto limitado + primera PC), alta identificación con la audiencia de 15-25 años, y el proceso de decisión bajo restricción es tensión narrativa natural.

---

## TOP 20 GENERAL (todas las ideas más fuertes)

01. 🟢⭐ A1-038 — FPS altos pero el juego se siente raro — curiosity gap perfecto, primera persona
02. 🟢⭐ A2M-011 — USB-C son iguales — creencia universal activa, consecuencia inmediata
03. 🟢⭐ A2M-004 — Modo incógnito invisible — creencia masiva, twist práctico
04. 🟢⭐ A2M-007 — Desfragmentar SSD — creencia activa con consecuencia real en hardware propio
05. 🟢⭐ A2D-009 — ISP cagando sin darte cuenta — injusticia económica, patrón viral validado
06. 🟢⭐ A2M-003 — Antivirus pago en 2025 — gasto evitable, twist económico claro
07. 🟢⭐ A2M-013 — Plan energía Balanced baja FPS — dato verificable, consecuencia gratis
08. 🟢⭐ A2M-016 — Thermal throttling solo en notebooks — creencia activa en desktop users
09. 🟢⭐ A2D-004 — Error más caro armando primera PC — conflicto del que está por armar
10. 🟢⭐ A2D-001 — Componente más peligroso y nadie lo dice — curiosity gap + twist contraintuitivo
11. 🟢⭐ A4S1-005 — PC no prendía por un tornillo suelto — causa oculta clásica, contable a cámara puro
12. 🟢⭐ A4S1-013 — Artefactos en pantalla: GPU o driver — curiosity gap masivo, altísimo share
13. 🟢⭐ A4S1-014 — PC se apagaba exactamente a las 3 horas — el "exactamente" crea gap poderoso
14. 🟢⭐ A4S2-004 — Upgradear vs armar de cero — decisión que enfrenta toda la audiencia
15. 🟢⭐ A4S2-001 — PC gamer de 500 USD para pibe de 15 — conflicto universal, alta identificación
16. 🟢⭐ A4S2-015 — Le armé la PC a mi viejo y ahora quiere jugar — twist emocional, WhatsApp-able
17. 🟢🔄 A1-011 — 32GB de RAM y Windows dice 16 — curiosity gap activo, adaptación a Formato A trivial
18. 🟢🔄 A1-035 — RAM 4800MHz corre a 2400 — mismo patrón viral bits/bytes, XMP no activado
19. 🟢🔄 A4S2-008 — Argentina vs USA en precios — injusticia económica, dato ancla necesario
20. 🟢🔄 A4S2-013 — La PC de un peso por componente — concepto original, curiosity gap activo

---

## Análisis por categoría (consolidado de los 5 agentes)

### 1. PRO vs PRINCIPIANTE (Agente 1 — 60 ideas)

001 🟢❌ - "Mi PC tiene más RGB que FPS" — Conflicto del viewer, twist implícito (gasta en estética, no en rendimiento), WhatsApp-able. Formato B nativo: el principiante defiende su RGB mientras la GPU cuelga. No funciona como Formato A porque el valor está en el diálogo de bardeo.

002 🟡🔄 - "Compré una PC GAMER en Marketplace" — Tema fuerte (estafa, miedo de masas), pero "compré" sin acción inminente ni conclusión equivocada pierde tensión. Reformular: "Me vendieron una PC gamer y la quiero devolver" + especificar el engaño concreto (i3 con RGB, sticker de gamer, etc.).

003 🟢❌ - "Le saqué todos los ventiladores porque hacían ruido" — Conclusión equivocada con acción inminente perfecta (ya los sacó). Twist: el ruido era señal de que algo andaba mal, no problema de los fans. Formato B puro: necesita el diálogo de diagnóstico ("¿Y por qué hacían ruido?").

004 🟢🔄 - "Instalé Windows en el disco equivocado" — Curiosity gap activo (el viewer que armó PC ya vivió el momento de elegir el disco), primera persona, frustración implícita. Funciona como Formato A (Modo 1: "¿Cómo sabés en qué disco está Windows?") o como Formato B. Se puede traducir a cámara con reformulación menor.

005 🟢❌ - "Le puse pasta térmica como manteca al pan" — Imagen concreta e hilarante, curiosity gap (el viewer sabe que hay que poner pasta pero no sabe cuánto). Formato B ideal: el PRO ve la pasta desbordada y el diagnóstico es inmediato. Incompatible con Formato A porque necesita el elemento visual de la pasta.

006 🟡🔄 - "No me enciende la PC nueva" — Tema universal pero formulación demasiado amplia, sin conclusión equivocada. Cae en "tutorial sin tensión" si se deja así. Reformular: especificar la conclusión equivocada ("La devolví a la tienda y era el cable de poder") o elegir una causa concreta (standoffs, fuente apagada, RAM mal asentada).

007 🟢❌ - "Compré DDR5 y mi mother es DDR4" — Conclusión equivocada perfecta con acción inminente (va a reclamar a la tienda). Curiosity gap activo: el viewer sabe que hay DDR4 y DDR5 pero no sabe que no son compatibles. Formato B nativo, necesita el diálogo de "¿me cagaron?".

008 🟢🔄 - "Conecté el monitor a la placa madre" — Conflicto del viewer, causa oculta (GPU dedicada idle), twist potente. Curiosity gap: el viewer que tiene GPU sabe que conectó algo pero no sabe por qué no anda bien. Funciona como Formato A Modo 1 ("Por qué el HDMI de la placa madre te limita los FPS?") o como Formato B.

009 🟠❌ - "No me entra el procesador" — Tema válido (LGA vs AM5, orientación del socket) pero sin tensión narrativa clara. La conclusión equivocada está implícita (forzarlo vs devolverlo) pero no está activada. Compite con ideas más tensas del banco. Solo funciona como Formato B con un hook muy específico.

010 🟡❌ - "Usé los tornillos equivocados en la mother" — Tema real (standoff sin tornillo de PC, madre cortocircuitada) pero formulación blanda. El conflicto existe pero no está activado. Reformular con consecuencia inmediata: "Mi PC nueva me daba patadas eléctricas" (que es la idea 051, ya ejecutada y validada). Muy similar a 051 — evaluar si es redundante.

011 🟢🔄 - "Tengo 32GB de RAM pero Windows dice 16" — Curiosity gap perfecto: el viewer compró 32GB, los metió, Windows dice 16. Gap específico y delimitado. Primera persona + frustración. Funciona como Formato A Modo 1 (explicación de dual channel + slot libre) o como Formato B.

012 🟢❌ - "Tengo una RTX 4070 y juego en 720p" — Conclusión equivocada con acción inminente: el principiante cree que "la GPU está mal". Twist: monitor conectado a la placa madre (o resolución configurada mal). Relacionada con 008 — revisar si son la misma idea antes de guionar. Formato B nativo.

013 🟢🔄 - "Compré un gabinete hermético porque era lindo" — Imagen concreta, twist claro (airflow = temperatura = throttling = menos FPS). Curiosity gap: el viewer que compró gabinete lindo no sabe por qué corre peor. WhatsApp-able. Adaptable a Formato A Modo 1 explicando por qué el airflow importa con el gabinete como ejemplo.

014 🟡🔄 - "Mi SSD NVMe no aparece" — Tema real y frecuente, pero la formulación es un síntoma, no una conclusión equivocada. Reformular: "Compré un SSD M.2 y no existe para la PC" + conclusión equivocada del principiante (lo devolví/está pinchado). Curiosity gap activo si se reformula con la causa oculta (slot PCIe en vez de NVMe, falta de inicialización en Windows).

015 🟢❌ - "Se me apaga jugando y no tira pantalla azul" — Excelente: causa oculta múltiple (PSU insuficiente, temperatura, RAM), twist en que la ausencia de BSOD confunde. Conclusión equivocada del principiante: "está todo bien porque no tira error". Formato B perfecto con diagnóstico progresivo.

016 🟢❌ - "Le dejé el plástico al cooler" — Imagen concreta e hilarante. Conclusión equivocada: la PC funciona aunque anda caliente, el principiante no sabe que el plástico está ahí. Primer frame visual poderosísimo (CPU a 100°C). Formato B nativo: el PRO descubre el plástico en el diagnóstico.

017 🟡❌ - "Puse todos los fans al revés" — Tema real (orientación del flujo), pero sin conclusión equivocada activa. El principiante simplemente no sabe. Reformular para que haya acción inminente: "Mis fans están todos prendidos pero la PC quema igual, voy a abrir para sacarlos todos" + twist de que el problema es la orientación, no los fans.

018 🟢❌ - "Mi juego usa 100% de CPU y la GPU está en 20%" — Curiosity gap perfecto: el viewer que tiene GPU sabe que algo no cuadra. Primera persona + frustración + causa oculta (cuello de botella de CPU, juego no optimizado, resolución baja). Formato B nativo con diagnóstico progresivo.

019 🟡❌ - "Conecté la GPU con un adaptador Molex" — Tema real y peligroso, pero "adaptador Molex" requiere contexto que no todos tienen. Reformular: "Conecté la GPU con el adaptador que venía en la caja y la fuente me quedó corta" o simplificar el hook para que sea más universal. Riesgo de caer en "in medias res sin setup".

020 🟢⭐ - "Tengo 100 megas y me baja a 2 MBs" — ✅ EJECUTADO (viral). Clasificación coincide con resultado: hook 8/10 en audit, primera persona + causa oculta (bits vs bytes) + curiosity gap activo. Formato A Modo 1 nativo y validado.

021 🟡🔄 - "Mi PC nueva ya está lenta" — Tema frecuente, pero formulación genérica sin imagen concreta. Cae en riesgo de "tutorial sin tensión". Reformular con causa concreta y conclusión equivocada: "Mi PC nueva va lenta, la voy a formatear" + twist (bloatware, XMP desactivado, disco HDD secundario como C:).

022 🔴🔄 - "Limpié la PC con la aspiradora" — Patrón flop: tutorial sin tensión. La situación es graciosa pero el video se convierte en "lo que no hay que hacer" = explicación = tutorial = saves. Sin conclusión equivocada activa con acción inminente. Si reformulás como "Limpié la PC y ahora no prende" (consecuencia), puede recuperarse.

023 🟠🔄 - "Mezclé RAM de distinta velocidad y marca" — Tema válido, pero el conflicto no está activado. El principiante no tiene una conclusión equivocada clara, solo hizo algo. Curiosity gap débil. Reformular: "Compré 8GB más de RAM de otra marca y ahora va más lento" + causa oculta (velocidad baja al peor stick). Compite con ideas de RAM más fuertes del banco (011, 035).

024 🟡🔄 - "No actualicé la BIOS y el procesador no arranca" — Tema real y frustrante, pero la formulación como "no actualicé" es confusa (el viewer promedio no sabe que BIOS necesita actualización para nuevos procesadores). Reformular: "Compré el procesador nuevo y la PC no arranca, me devuelven la placa" + twist (BIOS desactualizada, solución sin reemplazar nada).

025 🟢🔄 - "Mi PC hace ruido de click" — Curiosity gap activo (viewer tiene PC que hace ruido extraño, sabe que algo pasa, no sabe qué). Causa oculta múltiple (HDD muriendo, cooler roto, cable tocando fan). Primera persona + urgencia. Funciona como Formato A ("¿Qué significa ese ruido?") o como Formato B.

026 🟢❌ - "Me corre todo pero con microstutters" — Excelente curiosity gap: el viewer tiene FPS altos, el juego se siente mal, no entiende por qué. Causa oculta técnica (VRAM overflow, shader compile, 1% lows). Primera persona + frustración específica. Formato B con diagnóstico técnico avanzado.

027 🟢❌ - "Gasté todo en la GPU y me sobró para un i3" — Conclusión equivocada clásica con acción inminente: el principiante tiene setup desbalanceado y cree que la GPU es lo único que importa. Twist: cuello de botella de CPU mata rendimiento. WhatsApp-able (la gente lo manda para defender su build). Formato B nativo.

028 🟠⭐ - "Nunca entré a la BIOS" — Tema con potencial (XMP, boot order, CPU settings) pero sin conclusión equivocada ni acción inminente. Sin tensión. Si se reformula como hook de injusticia ("Pagaste por velocidad de RAM y nunca la activaste") puede funcionar como Formato A. Por ahora 🟠 porque la formulación actual no activa nada.

029 🟡🔄 - "Compré una mother cara y no me deja hacer overclock" — Tema real (chipset B vs Z, AMD vs Intel OC) con frustración genuina. Pero sin conclusión equivocada específica. Reformular: "Compré la mother más cara del segmento y me la bloquearon" + twist (Intel solo OC en Z-series, el vendedor no lo aclaró). Curiosity gap activo para quien ya tiene placa.

030 🟠🔄 - "Mi PC nueva tartamudea en todo" — Similar a 021 y 026, riesgo de superposición. La formulación vaga lo deja sin gancho específico. Necesita causa concreta para diferenciarse. Marcado 🟠 hasta que se especifique el twist (shader stutter vs VRAM vs HDD como disco de Windows).

031 🟠⭐ - "Me dijeron que el i5 es malo" — Tema válido (mito de jerarquía de nombres Intel/AMD) pero formulación como opinión ajena. Cae en riesgo de "reacción a contenido externo" si no se ancla en primera persona. Reformular: "Estaba por comprar un i5 y me dijeron que era basura" → primera persona + conclusión equivocada activada.

032 🟡🔄 - "Actualicé la BIOS y se me murió todo" — Tema real y dramático con tensión natural. Pero la formulación implica que algo salió mal en el proceso, no que el viewer tiene una conclusión equivocada. Reformular para que el principiante esté a PUNTO de actualizar la BIOS porque alguien se lo dijo, y el PRO frena: "¿Esperá, por qué lo estás actualizando?". Así el conflicto es previo a la catástrofe.

033 🟢🔄 - "Mi GPU nueva no entra en el gabinete" — Curiosity gap: el viewer compró GPU, el gabinete "es grande", no entra. Causa oculta (largo de GPU vs espacio de cables, bracket del HDD, etc.). Primera persona + frustración. Funciona como Formato A ("Antes de comprar una GPU, medí esto") o como Formato B con el diagnóstico en vivo.

034 🟡❌ - "Puse el cooler AIO con los tubos para arriba" — Tema técnico válido (air bubbles en el loop, ruido de bomba) pero requiere conocimiento previo sobre AIOs que no toda la audiencia tiene. Riesgo de "in medias res sin setup". Reformular para bajar la barrera: "Mi cooler de agua hace ruido y burbujea, lo devolví" + twist (los tubos miraban para arriba = aire en la bomba).

035 🟢🔄 - "Compré RAM de 4800MHz y corre a 2400" — Muy similar al viral de 020 (bits vs bytes) en estructura: compré X, me da Y. Curiosity gap activo (XMP/EXPO no activado). Primera persona + frustración. Funciona como Formato A Modo 1 o como Formato B. Revisar que no sea redundante con 011.

036 🟠⭐ - "Mi SSD nuevo tiene menos capacidad de la que dice" — Tema real (GiB vs GB, partición de recuperación) pero sin tensión narrativa fuerte. El viewer no tiene una conclusión equivocada accionable, solo confusión. Curiosity gap parcialmente activo. Potencial como Formato A Modo 1 corto, pero compite con ideas más tensas.

037 🟠🔄 - "Se me quemó la mother por una descarga" — Tema importante (tierra eléctrica, protectores de tensión, UPS) pero la formulación implica que ya pasó. Sin acción inminente. Compite con 051 (ya ejecutado y validado con standoffs). Necesita más contexto para diferenciarse.

038 🟢⭐ - "Tengo FPS altos pero el juego se siente raro" — Curiosity gap excelente: el viewer tiene PC gamer, tiene FPS altos, pero algo no cuadra. Causa oculta (VSync, Hz del monitor, 1% lows, input lag). Primer persona + desconcierto. Funciona perfecto como Formato A Modo 1 ("Por qué los FPS altos no garantizan que el juego se sienta bien").

039 🟠🔄 - "Mi PC no tiene WiFi" — Tema válido pero la formulación es plana, sin twist. El conflicto es obvio (no tiene WiFi porque no tiene adaptador o placa con WiFi). Reformular para que la conclusión equivocada sea activa: "Compré una placa que 'incluye WiFi' y no tenía antena" o "Cambié la mother y perdí el WiFi". Por ahora 🟠.

040 🟢❌ - "Compré la fuente más barata porque total es una fuente" — Conclusión equivocada perfecta con consecuencia inminente. Twist: PSU barata = componentes en riesgo, eficiencia 80 Plus, ripple. WhatsApp-able (la gente lo manda a amigos que están por armar PC). Formato B nativo con resistencia activa del principiante ("pero si total es una fuente, no hace nada especial").

041 🟢🔄 - "Mi PC huele a quemado pero funciona" — Curiosity gap activo: el viewer tiene PC que huele raro, sigue funcionando, no sabe si apagar o no. Primera persona + urgencia real. Causa oculta (capacitor, cable, GPU). Funciona como Formato A ("¿Qué hacer cuando tu PC huele a quemado?") con hook de urgencia o como Formato B.

042 🟢❌ - "Usé los cables de mi fuente vieja en la nueva" — ✅ EJECUTADO (Formato B validado). Clasificación coincide: conclusión equivocada con riesgo real (cables no son universales entre marcas = componentes quemados). Formato B nativo y validado empíricamente.

043 🟠🔄 - "El monitor se me ve amarillo" — Tema real (temperatura de color, Night Light activado, cable incorrecto) pero sin tensión fuerte. Sin conclusión equivocada accionable. El viewer no va a tomar ninguna acción dramática por un monitor amarillo. Necesita más contexto o causa específica para activar el conflicto.

044 🟠⭐ - "Mi GPU mina crypto sola" — Tema con potencial (GPU scheduling, DWM, procesos en background) pero la formulación suena a trivia o conspiracy. Sin tensión personal. Reformular como "Windows le está robando GPU a tus juegos" para activar injusticia económica. Por ahora 🟠 hasta reformulación.

045 🟠🔄 - "Tengo 2TB de SSD y me quedan 50GB" — Tema válido pero sin twist real: el viewer simplemente llenó el disco. El conflicto es de él pero la causa no es oculta. Reformular con causa inesperada: "Windows se comió 300GB solo" (archivos de hiberna, page file, WinSxS) para activar el curiosity gap.

046 🟢❌ - "Desactivé el antivirus para ganar FPS y me agarré un virus" — Conclusión equivocada con consecuencia ejecutada: el principiante tomó una acción lógica (para él) y pagó el precio. Twist doble: el antivirus moderno casi no consume FPS + ya tiene virus. WhatsApp-able. Formato B nativo con diagnóstico post-hecho.

047 🟡❌ - "La GPU se cae del slot por el peso" — Tema real (soporte de GPU, slot PCIe doblado) pero sin conclusión equivocada activa. El principiante no está por tomar ninguna acción incorrecta. Reformular: "Mi GPU se inclinó y dejó de funcionar, la devolví" + twist (soporte de GPU = solución de $5 vs RMA innecesario). Potencial bajo a medio.

048 🟢🔄 - "Compré un monitor 4K para jugar y no me dan los FPS" — Curiosity gap activo: el viewer compró el monitor "mejor", no entiende por qué rinde menos. Primera persona + frustración. Funciona como Formato A Modo 1 ("Por qué una GPU que corría bien a 1080p no alcanza para 4K") o como Formato B.

049 🟠🔄 - "Mi disco D desapareció" — Tema real (diskpart, actualización de Windows, asignación de letras) pero sin tensión dramática. El viewer no sabe si perdió datos o no. Si se enfoca en el miedo a pérdida de datos, puede funcionar. Necesita más contexto sobre la causa concreta.

050 🔴❌ - "Le puse dos GPUs para que rinda el doble" — Patrón flop: trivia sin conflicto real. SLI/NVLink está muerto como tecnología. El viewer promedio no tiene dos GPUs. Sin curiosity gap activo (no es un problema que el viewer esté viviendo). Descartar o reconvertir a anécdota histórica del "por qué SLI murió".

051 🟢❌ - "El gabinete me dio una patada eléctrica" — ✅ EJECUTADO (Formato B validado con standoffs). Clasificación coincide: conclusión equivocada perfecta (el gabinete está defectuoso = acción inminente de devolución) + causa oculta (standoffs faltantes = tierra eléctrica). Validado empíricamente.

052 🟡🔄 - "Compré un UPS barato y se me sigue cortando la PC" — Tema real (UPS de baja capacidad para PC de alta potencia) con frustración genuina. Pero el twist técnico (VA vs W, potencia real de la PC) es árido si no se hace con imagen concreta. Reformular: "El vendedor me dijo que con ese UPS me alcanzaba" + causa real (cálculo de VA/W mal hecho).

053 🟢🔄 - "Tengo pantalla azul pero solo cuando hace frío" — Curiosity gap excelente: síntoma específico y extraño (cold boot crash = RAM, pasta térmica, capacitor). Primera persona + situación concreta. WhatsApp-able ("mirá esto que me pasa"). Funciona como Formato A Modo 1 o como Formato B.

054 🔴🔄 - "Formateé y ahora el juego me pide comprarlo de nuevo" — Patrón flop: tutorial sin tensión. El video termina siendo "cómo funcionan las licencias digitales" = explicación = saves. Sin twist, sin causa oculta. Si reformulás desde la injusticia ("Steam/EpicGames se quedó con mi juego pagado") puede recuperarse mínimamente como Formato A de injusticia económica.

055 🟡🔄 - "Mi PC prende pero no sale imagen" — Tema frecuente y válido pero sin conclusión equivocada específica. Muy amplio (monitor apagado, cable suelto, GPU no asentada, driver). Reformular con causa única concreta: "Armé la PC, todo prende con luces y ruido del BIOS, pero pantalla negra" + causa = GPU a medias en el slot.

056 🟠❌ - "El disipador vino con pasta térmica pero le puse más encima" — Similar a 005 (pasta como manteca). Revela el mismo error desde ángulo diferente, pero compite directamente. Si 005 ya está en pipeline, esta es redundante. Marcado 🟠 por superposición con idea más fuerte del banco.

057 🟡🔄 - "Mi teclado mecánico suena como una ametralladora en Discord" — Hook con imagen concreta e hilarante. Pero el conflicto es periférico (lúber, switches), no de PC en sí. Reformular: anclar en consecuencia real ("Me mutean en cada call", "Mi equipo de ranked me odia") para activar identificación social. Potencial de Formato B con diagnóstico de switches.

058 🟢❌ - "Compré un procesador usado y tiene pines doblados" — Conclusión equivocada con acción inminente: el principiante cree que "lo cagaron" y va a pedir devolución/garantía. Twist: los pines se pueden enderezar con una tarjeta de crédito (o es culpa del comprador si no lo inspeccionó). Curiosity gap activo. Formato B nativo con diagnóstico en vivo.

059 🔴⭐ - "¿Por qué tu RAM tiene agujeros? (tema MetaPCs)" — Patrón flop: reacción a contenido externo. La idea explícitamente referencia MetaPCs = asume audiencias solapadas = validado en audit como flop (DLSS 5 reaction, 4/10). Descartar esta formulación. El tema de los agujeros en RAM (ranuras de ventilación) puede rescatarse como Formato A Modo 1 standalone sin mencionar MetaPCs.

060 🟡🔄 - "Me sobran cables de la fuente, ¿qué hice mal?" — Curiosity gap con potencial: el viewer que armó PC tiene cables sobrando y no sabe si hizo algo mal. Primera persona + ansiedad leve. El twist (los cables modulares son extra, no todos se usan) es corto pero válido. Reformular con más tensión: "Me sobraron cables de la fuente y no sé si algo no conecté" para activar la urgencia.

---

### 2. Directo a cámara (Agente 2 — primera mitad)

001 🟢⭐ - "El componente más peligroso de tu PC y nadie te lo dice" — Curiosity gap activo (el viewer tiene PC y asume que ya sabe qué puede fallar), twist obligado al revelar un componente contraintuitivo (ej. fuente de poder, no la GPU), WhatsApp-able porque genera conversación; formulación ya tiene tensión cognitiva y funciona directo a cámara Modo 1.

002 🟡⭐ - "Dejá de comprar PC por specs, comprá por uso" — El tema es fuerte pero la formulación cae en tutorial sin tensión (nadie siente dolor activo por "comprar por specs"); reformular con conflicto en primera persona del viewer: "Te estafaron con specs que nunca ibas a usar."

003 🟡⭐ - "Por qué las GPUs usadas de minería no dan tanto miedo" — Tema contra-narrativa válido pero el hook asume que el viewer ya tiene la creencia activa de que son peligrosas, sin activarla primero; reformular como: "Te dijeron que una GPU de minería te iba a durar dos meses. Mentira." — activa el conflicto antes de desmontarlo.

004 🟢⭐ - "El error más caro que podés cometer armando tu primera PC" — Conflicto del viewer (alguien que está por armar o armó), gap delimitado ("el" error, no "errores"), WhatsApp-able porque los que armaron quieren saber si lo cometieron; pasa el test de identificación social si la apertura es en primera persona del comprador.

005 🟢⭐ - "No existe la PC future-proof" — Afirmación provocadora que contradice la creencia del viewer que invirtió o está por invertir; genera twist ("gasté más para no tener que gastar más, y igual voy a gastar"), WhatsApp-able entre los que están convenciendo a alguien de comprar caro.

006 🟡⭐ - "¿Cuándo conviene comprar usado y cuándo nuevo?" — Como está formulado es un tutorial de consulta (guarda, no comparte); reformular con conflicto activo: "Compraste nuevo cuando tendrías que haber comprado usado. O al revés." — pone el error en el viewer antes de resolver.

007 🟢⭐ - "La GPU que todos ignoran y es la mejor relación precio-rendimiento" — Curiosity gap fuerte (el viewer ya está eligiendo GPU y asume que conoce las opciones), tiene un twist implícito (la mejor opción no es la obvia), WhatsApp-able porque la gente lo manda a quien está por comprar; riesgo: si la GPU que se revela es divisiva, pierde peso — la ejecución debe ser concreta con dato ancla verificable.

008 🟠🔄 - "DLSS, FSR, XeSS — ¿cuál uso y cuándo?" — Pasa el filtro mínimamente (viewer con GPU ya instalada y sin saber cuál activar), pero el formato de "cuál uso y cuándo" es una guía de consulta que genera saves, no shares; además compite con contenido ya masivo en inglés (Linus, Nate Gentile). Requiere ángulo lateral que hoy no tiene formulado.

009 🟢⭐ - "Tu ISP te está cagando y no te das cuenta" — Conflicto del viewer (paga internet, percibe que anda lento pero no conecta el problema con el ISP), emoción activa de indignación, WhatsApp-able porque la gente lo manda cuando le pasa lo mismo; Curiosity gap activo (hay un mecanismo oculto que explica por qué te cagan). Hay un viral validado en el audit con el mismo esquema (hook score 8/10).

010 🟡🔄 - "Pagar más por estética RGB es tirar la plata" — El tema es correcto pero la formulación es la opinión del creador, no el conflicto del viewer; reformular: "Me gasté $X de más en RGB que no impactan nada el rendimiento" — primera persona, costo concreto, viewer que se identifica con la compra.

011 🟠🔄 - "Lo primero que tenés que hacer cuando armás una PC nueva" — Tutorial puro sin tensión; no hay conflicto activo, no hay twist, genera saves no shares; necesitaría una causa oculta o consecuencia grave para no hacerlo que justifique el formato.

012 🟢⭐ - "Por qué tu PC de 5 años le gana a una notebook nueva" — Afirmación provocadora que contradice la creencia del viewer (la notebook nueva tiene que ser mejor por ser nueva), gap delimitado, WhatsApp-able para mandar al familiar que quiere tirar la desktop; pasa los 3 filtros.

013 🟠🔄 - "Las 3 cosas que reviso antes de comprar CUALQUIER componente" — Lista de tips, genera saves no shares; el viewer que ya sabe no lo comparte, el que no sabe lo guarda; necesita reformulación completa para tener conflicto activo.

014 🟢🔄 - "Por qué tu PC de escritorio necesita un SAI/UPS" — Curiosity gap válido (el viewer tiene desktop y nunca lo conectó a un UPS, no sabe qué consecuencia tiene), conflicto potencial fuerte si se abre con la consecuencia concreta ("Perdí trabajo / componentes por un corte de luz de 2 segundos"); A-Adaptable porque necesita dato ancla concreto y apertura en primera persona para que funcione.

015 🔴⭐ - "Dejá de limpiar la pantalla con cualquier cosa" — Patrón flop: tutorial sin tensión. La formulación es un consejo preventivo sin conflicto activo; nadie que limpia bien la pantalla lo comparte, y el que la limpia mal no sabe que lo hace mal hasta que la raya — en ese punto ya no sirve el video.

016 🟡⭐ - "El mito de que AMD calienta más que Intel" — Tema válido pero formulado como corrección de trivia; para tener conflicto activo el viewer tiene que tener esa creencia y que desmontarla le genere consecuencia práctica; reformular: "Estás perdiendo rendimiento por creer algo que era verdad en 2018 pero ya no lo es."

017 🟢⭐ - "5 señales de que tu PC se va a morir pronto" — Curiosity gap fuerte (el viewer tiene PC y teme perder datos/componentes), twist implícito en las señales que nadie reconoce como peligrosas, WhatsApp-able porque la gente lo manda cuando alguien tiene PC vieja; riesgo menor: que las señales sean las obvias (calor, lentitud) en lugar de las contraintuitivas.

018 🟠🔄 - "Qué GPU comprar en 2025 según tu presupuesto" — Guía de compra pura; genera saves, no shares; compite con contenido masivo en el nicho; para MOBO solo funciona si hay un ángulo local (precio en Argentina, disponibilidad en Mar del Plata) que hoy no está en el título.

019 🟢⭐ - "No compres un monitor gamer de 24 pulgadas en 2025" — Afirmación provocadora con consecuencia práctica para quien está por comprar, conflicto del viewer (está buscando monitor, todos le dicen 24"), WhatsApp-able para mandar al amigo que está eligiendo; pasa los 3 filtros.

020 🟡⭐ - "Por qué el cable DisplayPort es mejor que HDMI para gaming" — El tema es bueno (Curiosity gap para quien ya tiene ambos cables o está eligiendo monitor), pero la formulación es explicativa-comparativa sin tensión activa; reformular con conflicto económico: "Estás usando el cable equivocado y te estás perdiendo [X] FPS/Hz sin saber."

021 🟠🔄 - "La verdad sobre los gabinetes baratos" — Formulación vaga; "la verdad sobre" es un patrón de título sin conflicto específico que no activa curiosity gap delimitado; necesita más contexto sobre qué consecuencia concreta tienen los gabinetes baratos para ser clasificable mejor.

022 🟢⭐ - "Windows 11 te espía más de lo que pensás" — Conflicto del viewer (tiene Windows 11, cree que ya configuró la privacidad, hay algo que no sabe), gap delimitado, WhatsApp-able porque genera indignación que se comparte; riesgo: que el desarrollo caiga en lista de opciones a desactivar (tutorial sin tensión) — la ejecución debe mantener el tono de denuncia.

023 🟡⭐ - "Cuánto dura realmente un SSD" — El tema tiene curiosity gap válido (el viewer tiene SSD y no sabe su vida útil real), pero "cuánto dura realmente" es una pregunta abierta que puede resolverse con datos o puede quedarse en abstracto; reformular con tensión: "El contador de tu SSD dice que te quedan X años. Esto es lo que no te dice ese número."

024 🔴⭐ - "Por qué no deberías armar una PC en enero" — Patrón flop: trivia sin conflicto. La razón probablemente es de mercado (precios post-Navidad, stock, etc.) pero el viewer no tiene ese problema activo salvo que esté planeando comprar en enero específico; fuera de temporada pierde todo valor y dentro de temporada es demasiado nicho.

025 🟡⭐ - "Ray Tracing ¿vale la pena o es puro marketing?" — El tema es fuerte pero la formulación es la pregunta del creador, no el conflicto del viewer; reformular como consecuencia concreta: "Activaste ray tracing y te bajó 40 FPS. Así sabés si valió la pena o te lo vendieron." — primera persona, dato concreto, conflicto activo.

026 🟢⭐ - "Cómo saber si te están vendiendo una GPU usada como nueva" — Conflicto del viewer (está comprando o compró GPU y no puede verificar), consecuencia económica real, WhatsApp-able porque la gente lo manda antes de que un amigo compre; curiosity gap fuerte (hay mecanismos verificables que el viewer no conoce).

027 🟡⭐ - "La mentira del 4K ¿vale la pena en 2026?" — Tema válido pero "¿vale la pena?" es una pregunta abierta sin conflicto previo activo; reformular con tensión: "Pagaste el doble por 4K. Esto es lo que el fabricante no te dijo sobre cuándo realmente lo ves." — activa la compra ya hecha como conflicto.

028 🟡❌ - "RTX 5080 vs RX 9070 XT ¿Nvidia nos está robando?" — El "¿nos está robando?" tiene potencial de indignación pero la comparación de modelos específicos es contenido de reacción a contexto externo (lanzamiento de GPUs) con vida útil muy corta; además el benchmark-vs-precio es terreno pisado por canales grandes; A-Incompatible porque necesita datos comparativos visuales o formato B para funcionar.

029 🟢🔄 - "No compres PCs armadas del supermercado" — Conflicto del viewer (alguien que está considerando esa opción o que la compró), consecuencia económica clara, WhatsApp-able porque la gente lo manda a familiares que están por comprar; A-Adaptable porque funciona mejor con elemento visual de la PC del super en frame o con datos de precio/componente.

030 🟠🔄 - "Cuidado con las placas de video baratas de Temu y AliExpress" — El conflicto existe pero la formulación es advertencia genérica sin causa oculta ni twist; el viewer que ya desconfía de Temu no necesita el video, el que confía no lo busca; necesitaría un caso concreto con consecuencia inesperada para tener gancho.

---

### 3. Mitos tech (Agente 2 — segunda mitad)

001 🟡⭐ - "Apagar y prender la PC seguido la arruina" — El viewer tiene la creencia (la hereda de mitos de electrónica antigua), pero el mito formulado así es una corrección de trivia sin consecuencia activa; reformular con el costo concreto de la creencia incorrecta: "Dejás la PC prendida toda la noche para no arruinarla. Calculá cuánto te cuesta eso en luz al año."

002 🟡⭐ - "Overclockear te quema el procesador" — El viewer que querría hacer OC no lo hace por este mito; para tener conflicto activo necesita que el viewer esté dejando rendimiento sobre la mesa; reformular: "Tenés un procesador que puede rendir 15% más gratis y no lo tocás porque te dijeron que se quema. Esto es lo que pasa realmente."

003 🟢⭐ - "Necesitás un antivirus pago en 2025" — Creencia activa y común (mucha gente paga por antivirus), consecuencia económica real (gasto recurrente evitable), twist claro (Windows Defender es suficiente para la mayoría), WhatsApp-able porque la gente lo manda al familiar que paga Kaspersky; pasa los 3 filtros y el Curiosity gap es fuerte.

004 🟢⭐ - "El modo incógnito te hace invisible en internet" — Creencia activa y extendida, el viewer la tiene y la usa asumiendo privacidad real, el twist tiene consecuencia práctica (tu ISP y empleador te ven igual), WhatsApp-able con alta probabilidad porque genera reacción de "no sabía eso"; pasa todos los filtros.

005 🟠⭐ - "Más núcleos de CPU = siempre mejor para juegos" — La creencia existe pero es menos activa que hace 5 años; el viewer más informado ya sabe que la frecuencia importa, el menos informado no está eligiendo CPU activamente; para ser 🟢 necesitaría estar anclado en una decisión de compra concreta que el viewer tiene ahora.

006 🟢⭐ - "Un SSD NVMe Gen5 te da más FPS que un Gen3" — Curiosity gap fuerte para el viewer que está eligiendo entre Gen3 y Gen5 o que ya compró el más caro asumiendo más FPS; twist concreto (en gaming la diferencia es 0-2 FPS, el cuello de botella no es el storage), WhatsApp-able porque desmonta una compra cara; dato verificable con benchmarks disponibles.

007 🟢⭐ - "Tenés que desfragmentar tu SSD" — Creencia activa (heredada del HDD), consecuencia real si el viewer lo hace (reduce la vida útil del SSD), twist con impacto práctico, WhatsApp-able; Curiosity gap activo porque el viewer "sabe" que hay que desfragmentar pero no sabe que aplica al revés con SSD.

008 🟡⭐ - "Dejar la PC prendida toda la noche la daña" — Mito válido pero la formulación es casi idéntica a la idea 001 de este bloque; reformular para separar el ángulo: enfocarse en el costo energético real (dato concreto en pesos/kWh Argentina) en lugar de en el daño al hardware, así los dos temas son distintos y complementarios.

009 🔴❌ - "PC gaming es demasiado caro, mejor una consola" — Patrón flop: no es un mito tech factual, es una opinión de valor con respuesta que depende de cada caso; cualquier resolución del video es discutible y genera debate sin twist limpio; además el formato "PC vs consola" está agotado en el nicho y compite con contenido masivo; A-Incompatible porque si funciona es en Formato B (debate estructurado).

010 🔴❌ - "Tenés que actualizar la PC cada año" — Patrón flop: trivia sin conflicto activo. El viewer que actualiza cada año lo hace por elección, no por creencia en que es necesario; el que no actualiza no siente el conflicto; sin un costo concreto y una decisión inminente del viewer, es consejo abstracto.

011 🟢⭐ - "Todos los cables USB-C son iguales" — Creencia activa y universal (el viewer tiene varios cables USB-C mezclados), consecuencia práctica real (carga lenta, datos lentos, sin video, sin carga en algunos dispositivos), twist con impacto inmediato, WhatsApp-able porque la gente lo manda cuando alguien tiene problemas con el cable; uno de los mejores del bloque.

012 🟠⭐ - "32GB de RAM es obligatorio para jugar en 2025" — El mito existe pero la dirección importa: el viewer que ya tiene 16GB y se siente deficiente tiene conflicto activo; el que ya tiene 32GB no tiene conflicto; como está formulado ataca la creencia de "obligatorio" pero sin anclarlo en la situación específica del viewer que tiene 16GB y se pregunta si upgradear.

013 🟢⭐ - "El plan de energía en Balanced te baja FPS" — Curiosity gap fuerte (el viewer tiene Windows en Balanced, nunca lo cambió, y no sabe que puede estar perdiendo rendimiento gratis), consecuencia verificable en FPS, WhatsApp-able porque la gente lo manda a quien tiene PC gamer; twist doble: Balanced sí afecta en algunos casos pero no en todos — eso es más interesante que "siempre baja".

014 🔴⭐ - "Formatear cada 6 meses es necesario" — Patrón flop: trivia sin conflicto. La creencia viene de Windows XP/7; en 2025 Windows no se degrada de la misma manera y el viewer moderno promedio no formatea ni sabe si lo necesita — no tiene una decisión activa de compra o uso bloqueada por este mito.

015 🟠🔄 - "Cerrar Chrome mejora el rendimiento en juegos" — La creencia existe pero el conflicto es débil porque el viewer que lo cree ya cierra Chrome (no tiene problema activo), y el que no lo hace no siente el impacto; para tener gancho necesita un ángulo específico como el proceso de fondo que Chrome deja corriendo incluso cerrado — ese sí es un dato oculto con consecuencia real.

016 🟢⭐ - "Thermal throttling solo pasa en notebooks" — Creencia activa en usuarios de desktop que nunca monitorearon temperaturas, consecuencia real (están perdiendo rendimiento sin saberlo), twist con impacto en hardware propio, WhatsApp-able; Curiosity gap fuerte porque el viewer tiene desktop y asume que está a salvo.

017 🔴🔄 - "Las Mac no tienen virus" — Patrón flop: trivia sin conflicto. El viewer que usa Mac no va a cambiar de sistema por esto; el que no usa Mac no le importa; además el tema está cubierto masivamente por canales de seguridad y tech; A-Incompatible para Formato A de MOBO porque MOBO es una tienda de hardware PC/gaming, no de Apple.

018 🟠🔄 - "Poner la PC en el piso es lo mismo que en el escritorio" — La creencia existe pero el conflicto es de baja intensidad para la mayoría del target; solo es relevante para entornos con alfombra o mucho polvo; como mito es demasiado situacional para ser WhatsApp-able masivamente. Requiere más contexto para clasificar mejor.

019 🟡🔄 - "WiFi 6 te da más velocidad de internet" — El mito es real (el viewer que compró router WiFi 6 asume que va más rápido) y tiene consecuencia práctica, pero la formulación es demasiado plana; reformular con el dato concreto que desmonta la creencia: "Pagaste $X por WiFi 6 para bajar más rápido. Esto es lo que en realidad compraste." — activa la compra ya hecha como conflicto.

020 🔴❌ - "Más megapíxeles = mejor cámara siempre" — Patrón flop: trivia sin conflicto para la audiencia de MOBO. El target es hardware PC/gaming, no fotografía ni smartphones; aunque el mito es válido como corrección técnica, no genera conflicto activo para el viewer de @mobomdp que viene por contenido de PC; A-Incompatible con el nicho de la cuenta.

---

### 4. Datos curiosos (Agente 3 — primera mitad)

> AVISO APLICADO: el audit tiene evidencia empírica directa de que "trivia sin conflicto" flopa (PS3 supercomputadora, 3/10). El archivo 09 confirma el mecanismo: si el viewer no tenía un gap previo activado sobre el tema, no hay curiosity gap posible. Apliqué este criterio sin excepciones.

001 🔴❌ - "WiFi nació de un intento de detectar agujeros negros" — Trivia sin conflicto: el viewer no tenía un gap activo sobre el origen del WiFi. El propio archivo 09 lo cita como ejemplo de fallo de curiosity gap.

002 🔴❌ - "Spam se llama así por Monty Python" — Trivia sin conflicto: nadie tiene un problema activo con el origen de la palabra "spam". Dato curioso, cero tensión.

003 🔴❌ - "El primer mouse de la historia era de madera" — Trivia sin conflicto: sin tensión del viewer, sin consecuencia para él. Es un dato de almanaque.

004 🟡🔄 - "Hay un lenguaje de programación que te obliga a decir POR FAVOR" — Reformular: el ángulo original es trivia pura, pero tiene potencial si se pivotea a "por qué los lenguajes de programación sí tienen 'reglas de cortesía' y Windows no te pide nada". El conflicto tiene que ser del viewer programador/usuario. Por sí solo es un dato sin tensión.

005 🟡⭐ - "Deep Blue le ganó a Kasparov por un bug" — Reformular: el dato tiene twist (la IA que revolucionó el mundo ganó por accidente) pero el hook está en tercera persona y asume que el viewer ya conoce la historia. Reformular como "¿Qué pasa si te digo que la IA más famosa de la historia ganó su partida decisiva porque falló?". Modo 2 Anécdota.

006 🟠🔄 - "Hay más dispositivos conectados a internet que personas en la Tierra" — Dudoso: tiene curiosity gap mínimo pero es un dato ampliamente difundido, pierde por saturación. Solo funciona si hay un twist sobre qué son esos dispositivos y qué implica para tu PC/red.

007 🟢⭐ - "Usar la PC te hace parpadear 3 veces menos" — ALTO: el viewer YA usa la PC y YA tiene ojos secos o cansados. Gap preexistente, causa oculta, consecuencia corporal concreta. Pasa los 3 filtros: conflicto del viewer (me afecta a mí), tiene twist (la causa es el parpadeo, no la luz), es WhatsApp-able ("mandáselo al que se pasa 8hs en la PC"). Test Curiosity Gap: sí/sí/sí.

008 🔴❌ - "ENIAC, la primera computadora electrónica, pesaba 27 toneladas" — Trivia sin conflicto: dato histórico sin tensión ni consecuencia para el viewer actual.

009 🔴❌ - "La primera programadora de la historia fue Ada Lovelace" — Trivia sin conflicto: histórico, sin gap activo del viewer, ya muy difundido.

010 🟡⭐ - "Bluetooth se llama así por un rey vikingo" — Reformular: el ángulo histórico tiene estructura de Modo 2 pero la idea está formulada como trivia plana. Funciona si el hook abre con la incongruencia ("¿Por qué tu auricular se llama igual que un rey vikingo del siglo X?") y el desarrollo conecta con la lógica de unificación. Tiene curiosity gap porque el viewer usa Bluetooth a diario.

011 🟡⭐ - "Google casi se llamó BackRub" — Reformular: formulado como trivia. Funciona si se reformula como storytelling empresarial (Modo 3): la decisión de cambiar el nombre, el error de tipeo que generó "Google", qué hubiera pasado con el SEO de "BackRub". El twist tiene que estar en la consecuencia, no en el dato.

012 🔴❌ - "El primer disco duro pesaba una tonelada" — Trivia sin conflicto: dato de almanaque sin tensión ni consecuencia para el viewer.

013 🔴❌ - "Los emoticones nacieron en 1982" — Trivia sin conflicto: sin gap activo, sin tensión, completamente inactivo para el viewer.

014 🟢⭐ - "El primer virus de PC se creó para PROTEGER software" — ALTO: tiene twist fuerte (lo que pensás que es un ataque nació como defensa), conecta con la experiencia del viewer (todos temen los virus), y el giro es WhatsApp-able. Curiosity gap: el viewer YA sabe qué es un virus, YA le genera miedo, no sabe el origen. Gap específico y resoluble.

015 🟢⭐ - "YouTube nació como un sitio de citas" — ALTO: el viewer usa YouTube a diario, el twist es fuerte e inesperado, y la pregunta "¿cómo pasaste de ser Tinder a ser YouTube?" es un gap resoluble. Modo 3 storytelling empresarial. WhatsApp-able, conflicto del viewer (te sorprende algo que usás todos los días).

016 🟢⭐ - "El CPU de tu celular es más potente que la computadora del Apollo 11" — ALTO: el viewer tiene ese celular en la mano ahora mismo. Gap preexistente (intuye que hay diferencia, no sabe la magnitud), causa oculta (qué implica eso sobre el progreso real), y es WhatsApp-able. Curiosity gap: sí/sí/sí. Pasa los 3 filtros de filtro general.

017 🔴❌ - "La arroba (@) era un símbolo de peso en el comercio medieval" — Trivia sin conflicto: histórico, sin gap activo del viewer cotidiano, dato circulado ampliamente.

018 🟠🔄 - "Nintendo empezó vendiendo cartas en 1889" — Dudoso: tiene estructura de storytelling (Modo 3) pero el viewer que le importa a MOBO es de hardware, no de gaming history. Compite con ideas mejores del banco. Funciona solo si el pivot conecta con por qué Nintendo sobrevivió 130 años y Sony/Sega no.

019 🔴❌ - "El CD fue diseñado para que entre la Novena Sinfonía completa" — Trivia sin conflicto: sin gap activo del viewer, sin consecuencia para él, formato físico obsoleto para la audiencia.

020 🟢⭐ - "QWERTY fue diseñado para que escribas MÁS LENTO" ✅ EJECUTADO (VIRAL) — ALTO: confirmado por resultado real. El audit valida esta clasificación. Tiene todos los elementos: gap preexistente (viewer usa teclado a diario), twist fuerte (lo que usás está diseñado en tu contra), WhatsApp-able.

021 🔴❌ - "Amazon empezó vendiendo solo libros" — Trivia sin conflicto: muy conocido, sin gap activo, sin tensión para el viewer.

022 🟢⭐ - "La contraseña más usada del mundo sigue siendo 123456" — ALTO: el viewer usa contraseñas todos los días. El gap es "¿la mía es de las malas?" más la identificación social de "todos lo saben y nadie lo cambia". Tiene twist de ironía (en 2026 todavía), es WhatsApp-able porque genera vergüenza ajena. Pasa los 3 filtros.

023 🔴❌ - "El primer email de la historia fue ilegible" — Trivia sin conflicto: sin gap activo del viewer, sin consecuencia para él.

024 🟢⭐ - "JPG destruye tu imagen cada vez que la guardás" — ALTO: el viewer guarda JPGs. El gap es directo: algo que hacés habitualmente te está costando calidad sin que lo sepas. Causa oculta, consecuencia concreta, WhatsApp-able. Curiosity gap: sí/sí/sí.

025 🟠⭐ - "Google.com estuvo sin registrar por unos minutos en 2015" — Dudoso: tiene twist pero el impacto del viewer es bajo (no podría haberlo comprado, no le afecta). Funciona solo si el hook se reformula como "¿cuánto vale un dominio que puede estar sin dueño 60 minutos?" y conecta con el valor de los dominios digitales.

---

### 5. Tips (Agente 3 — segunda mitad)

> AVISO APLICADO: el audit tiene evidencia empírica directa de que "tip puro" flopa (Tip para limpiar PC, 2/10). La estructura de XBOX Game Bar (240K views) funcionó porque envolvió el tip en conflicto del viewer con conclusión equivocada. Apliqué este criterio con rigor.

001 🟡❌ - "Desactivá Memory Integrity en Windows para ganar 5-7% de FPS" — Reformular: tiene conflicto real del viewer (quiero más FPS), pero formulado como instrucción pura. Funciona como Formato B: el principiante tiene Memory Integrity activada por default, el PRO le pregunta "¿para qué lo tenés activado?". El conflicto es "Windows me está robando FPS y yo no lo sé". La adaptación directa a cámara sin diálogo pierde la tensión.

002 🔴🔄 - "Win+Shift+S es captura de pantalla instantánea" — Tutorial sin tensión: tip de atajo, sin conflicto del viewer, sin causa oculta. El viewer no tiene un problema activo con capturas de pantalla.

003 🟡❌ - "Configurá las curvas de ventiladores en la BIOS" — Reformular: tiene conflicto potencial (tu PC hace ruido o se calienta y no sabés por qué), pero formulado como instrucción técnica. El hook tiene que arrancar desde el problema del viewer: "¿Por qué tu PC hace ese ruido a las 2 de la mañana?" El tip es la solución, no el hook.

004 🟡❌ - "Desactivá la aceleración del mouse para apuntar mejor en shooters" — Reformular: tiene conflicto del viewer gamer (apunto mal y no sé por qué), pero es tip puro. Funciona como Formato B: el principiante culpa al aim, el PRO le pregunta "¿tenés la aceleración del mouse activada?". En Formato A no tiene gancho suficiente.

005 🔴🔄 - "Activá Game Mode en Windows" — Tutorial sin tensión: tip genérico, ya sobreexplotado, sin twist, sin conflicto del viewer. Game Mode apenas mueve la aguja y es la solución que todos conocen.

006 🔴🔄 - "Ctrl+Shift+Esc abre el Administrador de Tareas directo" — Tutorial sin tensión: atajo de teclado puro, sin conflicto del viewer, sin causa oculta. Igual que Win+Shift+S.

007 🟢❌ - "Poné tus juegos en pantalla completa exclusiva, no Borderless Windowed" — ALTO: el viewer gamer YA eligió Borderless sin saber las consecuencias. Gap preexistente (uso un modo que parece mejor y rinde peor), causa oculta (exclusivo tiene acceso directo a GPU), consecuencia concreta en FPS. Necesita Formato B o el sub-formato de lectura de comentario para Formato A, no funciona como Formato A estándar.

008 🔴🔄 - "Dynamic Lock bloquea tu PC cuando te alejás" — Tutorial sin tensión: feature de Windows que nadie necesita urgentemente, sin conflicto activo del viewer.

009 🟡🔄 - "Revisá qué programas arrancan con Windows" — Reformular: el conflicto del viewer existe (PC lenta al arrancar) pero la formulación es instrucción pura. Reformular como "¿Por qué tu PC tarda 3 minutos en arrancar si la compraste hace un mes?". El tip es la resolución, no el hook.

010 🔴🔄 - "Snap Layouts para organizar ventanas al instante" — Tutorial sin tensión: tip de productividad sin conflicto del viewer, sin causa oculta.

011 🔴🔄 - "Limpiá tu PC con aire comprimido cada 3 meses" — Tutorial sin tensión: validado empíricamente en el audit como flop exacto (Tip para limpiar PC, 2/10). Mismo patrón, mismo destino.

012 🟢❌ - "Activá PBO o MCE en la BIOS si tenés buen cooler" — ALTO: el viewer con CPU AMD tiene rendimiento que se está dejando arriba de la mesa sin saberlo. Gap preexistente, causa oculta, consecuencia medible. Requiere Formato B: el principiante no sabe que el fabricante pone límites conservadores de fábrica. No funciona en Formato A sin diálogo.

013 🟡🔄 - "Chequeá las temperaturas con HWMonitor gratis" — Reformular: el conflicto existe (¿cómo sé si mi PC se está cocinando?) pero es instrucción pura. Reformular desde el problema: "¿Cómo sabés si tu PC está a punto de morir por temperatura?". El tool es la solución, no el hook.

014 🟢⭐ - "Usá Ethernet en vez de WiFi para jugar online" — ALTO: el viewer gamer sufre lag activamente. Gap preexistente (pago buena conexión y me lagguea), causa oculta (WiFi tiene latencia variable que el cable no tiene), consecuencia concreta. Funciona en Formato A como explicación técnica. WhatsApp-able ("mandáselo al que se queja del lag").

015 🟢⭐ - "Desactivá la Xbox Game Bar si no la usás" ✅ EJECUTADO (VIRAL: 240K views) — ALTO: confirmado por resultado real. El audit lo cita como ejemplo de tip envuelto en conflicto del viewer con conclusión equivocada. Clasificación validada.

016 🟡🔄 - "Cambiá el DNS a 1.1.1.1 o 8.8.8.8" — Reformular: tiene conflicto del viewer (internet lenta o insegura) pero formulado como instrucción sin tensión. Reformular desde "¿Por qué tu proveedor de internet te asigna un DNS que te hace ir más lento?". La causa oculta (el ISP tiene incentivos para no darte el mejor DNS) es el hook.

017 🔴🔄 - "Win+V activa el historial de portapapeles" — Tutorial sin tensión: atajo de teclado sin conflicto activo del viewer.

018 🟠🔄 - "Configurá un segundo escritorio virtual para streamear" — Dudoso: audiencia nicho (streamers), sin conflicto universal, y el setup de dos escritorios es conocido. Solo funciona si hay un conflicto concreto de streamer ("¿por qué aparece tu Discord en el stream cuando no querés?").

019 🔴🔄 - "Actualizá drivers de GPU desde la página oficial de Nvidia/AMD" — Tutorial sin tensión: instrucción básica sin conflicto ni twist. El viewer ya sabe que hay que actualizar drivers.

020 🟡⭐ - "Snipping Tool en Windows 11 tiene OCR" — Reformular: tiene un twist genuino (una herramienta que usás para capturar imágenes también puede leer texto), pero formulado como dato plano. Reformular como "¿Sabías que podés copiar texto de una imagen en Windows sin instalar nada?". El conflicto del viewer es real (quiero copiar texto de una foto y no sé cómo). En Formato A funciona si el hook arranca desde el problema del viewer.

---

### 6. Storytime arreglo (Agente 4 — primera mitad)

001 🟡🔄 - "La PC del ciber que llevaba 6 años sin limpiar" — El tema es fuerte y visualmente brutal, pero el hook como está nombrado es del creador (Santi mirando el ciber), no del viewer; reformular a "¿Cuándo fue la última vez que limpiaste tu PC? Abrí una que llevaba 6 años sin tocar."

002 🟡🔄 - "El cliente que fumaba al lado de la PC" — Historia de cliente raro, cae en "in medias res sin setup" si no hay un puente claro con el viewer; reformular al conflicto del viewer: "Lo que el cigarrillo le hace a los componentes que nadie te dice."

003 🟢🔄 - "La PC que tenía una cucaracha adentro" — Conflicto del viewer (miedo latente, todos evitan limpiar), tiene twist visual garantizado, WhatsApp-able; necesita hook en primera persona con emoción activa ("Abrí una PC y había algo que no debería estar ahí").

004 🟠❌ - "El pibe que trajo la PC partida en dos" — Historia de cliente, conflicto es del creador que observa, no del viewer que se identifica; sin imágenes del estado físico el impacto cae a la mitad, necesita B-roll real para funcionar.

005 🟢⭐ - "La PC que no prendía por un tornillo suelto" — Curiosity gap activo (todos han visto una PC que no prende), causa oculta inesperada, resoluble en 30-45s, se puede contar a cámara puro ("Un cliente me trajo una PC que no prendía. El diagnóstico me llevó 4 horas. El arreglo, 10 segundos.").

006 🟡🔄 - "La notebook del estudiante con 47 virus" — El número "47" es el hook, pero el foco está en el estudiante, no en el viewer; reformular a "¿Cómo sabés si tu PC tiene virus? Esta tenía 47 y la dueña no lo sabía."

007 🟠❌ - "El AIO que se filtró y mojó la GPU" — Tema técnico con alta especificidad, pero sin imágenes del desastre el story pierde impacto; el viewer que no tiene AIO no se identifica.

008 🟡🔄 - "El gato le arrancó los cables a la PC" — Visualmente gracioso y WhatsApp-able, pero el conflicto es del dueño del gato ausente; reformular a identificación universal: "Si tenés gato y tenés PC, mirá esto" (etiqueta arquetipo).

009 🟠🔄 - "Restaurando una PC de hace 15 años" — Curiosidad histórica válida, pero sin conflicto activo del viewer cae cerca de "trivia sin conflicto"; funciona si el pivot es "y terminó corriendo X juego actual", sin eso es dudoso.

010 🟡🔄 - "La PC gamer que usaban de servidor 24/7" — Buena tensión latente (todos tienen miedo de dejar la PC prendida), reformular hook a conflicto del viewer: "¿Le hace mal a tu PC estar encendida todo el día?" — ahí pasa de historia a desmitificación con anécdota.

011 🟢🔄 - "Limpieza extrema: la PC de taller mecánico" — Muy visual, WhatsApp-able, curiosity gap activo (el viewer nunca imaginó ese nivel de suciedad), conflicto universal (miedo a la suciedad propia); necesita imágenes pero el hook se puede lanzar a cámara.

012 🟠❌ - "El cliente que metió la PC en una bolsa para mudarla" — Historia de cliente raro sin puente al viewer, cae en "in medias res sin setup"; sin imágenes del estado de llegada el impacto es casi nulo.

013 🟢⭐ - "Artefactos en pantalla: GPU muriendo o driver malo" — Curiosity gap perfecto: todos los que gamen vieron artefactos y no saben si es grave; causa oculta (puede ser trivial o catastrófica), resoluble a cámara en 45s, shares altísimos porque el viewer le manda el video a cualquier amigo con el problema.

014 🟢⭐ - "La PC que se apagaba exactamente a las 3 horas" — El detalle "exactamente" crea el gap (patrón = causa oculta), conflicto del viewer (todos tuvieron una PC con comportamiento extraño), resoluble con explicación técnica en tiempo corto, muy WhatsApp-able.

015 🟡🔄 - "Rescatando los datos de un HDD que hace click" — El "click de la muerte" tiene awareness universal entre gente con PC, pero el story como está es del creador realizando el rescate; reformular a "¿Tu HDD hace click? Lo que eso significa y cuánto tiempo tenés."

016 🟠🔄 - "El overclock que derritió el VRM" — Tema de nicho (overclockers), el viewer general no se identifica; funciona como advertencia si el hook apunta al viewer que quiere hacer OC, no como storytime genérico.

017 🟡🔄 - "La fuente genérica que explotó literalmente" — Alta carga emocional y WhatsApp-able, pero el hook como historia de otro cae en "in medias res sin setup"; reformular a conflicto del viewer directo: "¿Tu fuente es genérica? Mirá lo que puede pasar."

018 🔴⭐ - "La PC de la abuela que anda lenta" — Patrón flop: "tutorial sin tensión". El viewer no tiene urgencia ni curiosidad activa sobre la PC ajena de una abuela; si no hay twist real (causa oculta sorprendente) es una explicación de optimización básica.

019 🟡⭐ - "El gabinete con airflow al revés" — Curiosity gap presente (muchos armaron su PC y no chequearon el airflow), pero el hook como anécdota de cliente no activa identificación; reformular a primera persona del viewer: "Armaste tu PC y resulta que el aire entra al revés. Cómo saberlo."

020 🟠❌ - "El liquid metal que se desparramó por la mother" — Nicho extremo (casi nadie usa liquid metal), sin identificación del viewer general; necesita imágenes del daño para funcionar como story, no funciona solo a cámara.

021 🟢🔄 - "Esta PC tenía un ecosistema adentro" — Hook de impacto visual máximo, universalmente WhatsApp-able, curiosity gap ("¿qué tan sucia puede estar tu PC?"); el título en modo "esto encontré" funciona como anzuelo pre-reproducción. Necesita algo de B-roll del "ecosistema".

022 🟡🔄 - "Reviví una PC de oficina HP para jugar al Cyberpunk" — Buena tensión (upgrade imposible = twist), pero la especificidad "HP de oficina" acota la audiencia; reformular a conflicto universal: "¿Se puede jugar al Cyberpunk con una PC de oficina vieja?" — ahí el viewer se identifica.

---

### 7. Storytime ensamble (Agente 4 — segunda mitad)

001 🟢⭐ - "PC gamer de 500 USD para un pibe de 15" — Conflicto del viewer universal (presupuesto limitado + hijo/hermano/uno mismo a los 15), causa oculta (qué sacrificar sin arruinar la experiencia), muy WhatsApp-able; se cuenta a cámara directo con el proceso de decisión como tensión.

002 🟡🔄 - "PC de edición de video con presupuesto gamer" — Tema fuerte (conflicto real del viewer creativo con plata de gamer), pero como storytime se dispersa; reformular a desmitificación directa: "Cuánto cambia priorizar RAM sobre GPU si editás video."

003 🟠🔄 - "La PC que armé con piezas 100% usadas" — Interesante pero sin conflicto activo del viewer; funciona si el hook es "¿Conviene armar con todo usado?" con números reales al final, no como historia de proceso.

004 🟢⭐ - "Upgradear vs armar de cero: qué convenía" — Curiosity gap perfecto (todos los que tienen PC hace años enfrentan esta decisión), conflicto del viewer, resoluble en 45s con un criterio claro, alto potencial de shares porque el viewer lo manda a quien está en esa situación.

005 🟡⭐ - "Mi primera PC: todos los errores que cometí" — Alta identificación (todos armaron mal su primera PC), pero el hook está en primera persona del creador, no del viewer; reformular a "Los errores que cometés cuando armás tu primera PC" para que el viewer se vea en el espejo, no mire la historia de otro.

006 🟠🔄 - "PC compacta ITX para el escritorio chico" — Nicho válido pero reducido; el conflicto del escritorio chico no es universal, y sin imágenes del proceso de instalación en espacio pequeño el story pierde la mitad del valor.

007 🟡🔄 - "La PC de streaming completa por menos de 800 USD" — Conflicto real del viewer que quiere streamear, pero el enfoque "menos de 800" compite con mil videos similares; reformular al twist: "Por qué el setup de streaming más barato no es lo que creés."

008 🟢🔄 - "Armamos la misma PC con precios de Argentina vs USA" — Curiosity gap altísimo (todos en Argentina conocen la diferencia pero no saben cuánto), conflicto injusticia económica (segundo hook más fuerte del audit), WhatsApp-able; necesita números reales como dato ancla.

009 🟠⭐ - "PC para el abuelo que solo usa email y YouTube" — El viewer no es el abuelo, es el nieto que tiene que resolver el problema; conflicto es del creador (yo te armo la solución), no del viewer. Funciona solo si el hook activa el conflicto del que tiene que armarle una PC a un familiar.

010 🔴❌ - "Armando una PC white aesthetic sin gastar de más" — Patrón flop: "tutorial sin tensión". No hay conflicto activo, no hay causa oculta, es una guía de compra estética. Sin twist no genera shares.

011 🟡🔄 - "La build silenciosa: 0 dB bajo carga" — El dato "0 dB" tiene curiosity gap (todos quieren PC silenciosa), pero el storytime de armado es largo y sin tensión; reformular a desmitificación: "Cuánto sale realmente una PC en silencio total."

012 🟠🔄 - "PC para diseño gráfico + gaming: el combo perfecto" — "Combo perfecto" es promesa genérica sin conflicto; el viewer que busca esto quiere saber qué sacrifica, no que existe una solución perfecta. Reformular con el trade-off como tensión.

013 🟢🔄 - "La PC de un peso por componente" — Concepto original, curiosity gap activo (nadie lo hizo así), twist en el resultado, WhatsApp-able porque es raro; necesita números reales de cuánto salió cada componente para que el dato ancla funcione.

014 🟡🔄 - "Upgrade path: cómo planear una PC que crece con vos" — Conflicto del viewer real (todos compraron algo que se quedó corto), pero el enfoque "cómo planear" lo convierte en tutorial; reformular con un caso concreto como hook: "Armé esta PC y en 2 años gasté la mitad que si la hubiera comprado completa."

015 🟢⭐ - "Le armé la PC a mi viejo y ahora quiere jugar" — Alta identificación, twist emocional real (el padre no gamer que se convierte), WhatsApp-able máximo; se cuenta a cámara en modo anécdota, el hook es la conclusión absurda y divertida.

016 🟡❌ - "El cliente desapareció y me dejó esta nave" — Visualmente potente si existe el hardware, pero como story a cámara sin mostrar la PC no funciona; si hay imágenes de la build abandoned es 🟢, sin ellas es "in medias res sin setup" — el viewer no tiene contexto de por qué le importa.

---

### 8. Tutoriales (Agente 5 — primera mitad)

001 🔴❌ - "Cómo armar tu primera PC paso a paso — Guía completa 2025" — tutorial sin tensión. El título es descripción pura, no conflicto del viewer. Compite directamente con Linus/Paul's Hardware. Genera saves, no shares.

002 🔴❌ - "Cómo cambiar la pasta térmica paso a paso" — tutorial sin tensión. Sin conflicto del viewer activo ("Tip para limpiar PC" flop 2/10 en audit = mismo patrón exacto). Proceso lineal sin twist posible.

003 🔴❌ - "Cómo instalar Windows 11 desde un USB" — tutorial sin tensión. Evergreen puro pero genera saves de archivo, no shares. Cualquier canal grande ya lo tiene cubierto.

004 🔴❌ - "Cómo limpiar tu PC correctamente sin romper nada" — tutorial sin tensión. "Tip para limpiar PC" fue el peor hook del audit (2/10). Este título lo replica casi literal. Patrón flop validado empíricamente.

005 🔴❌ - "Cómo instalar un AIO liquid cooler" — tutorial sin tensión. Requiere demostración visual paso a paso. Sin conflicto del viewer en el título. Proceso técnico lineal = saves, no shares.

006 🟡🔄 - "Cómo configurar la BIOS después de armar tu PC" — tema fuerte porque tiene confusión real del viewer (creyeron que con armar alcanzaba). Reformulación: "Armé mi PC y no le configuré nada en la BIOS. ¿Qué le pasó después?" — conflicto en primera persona + causa oculta.

007 🟡🔄 - "Cómo upgradear la GPU sin romper nada" — el "sin romper nada" sugiere un miedo real del viewer, pero el título no activa el gap. Reformulación: "Cambié la GPU y la PC no arrancó. El problema no era la placa." — el twist tiene que estar en el hook, no implícito.

008 🔴❌ - "Cómo hacer cable management como un profesional" — tutorial sin tensión. Aspiracional-estético sin conflicto funcional. Genera saves de "referencia", no shares. Interés es del creador mostrar skill, no del viewer resolviendo un problema activo.

009 🟠🔄 - "Cómo testear tu PC nueva para asegurarte que todo funciona" — hay un conflicto potencial real ("¿cómo sé que no me vendieron algo defectuoso?") pero como está formulado es tutorial lineal. Necesita más contexto: si el ángulo es "me estafaron con una parte defectuosa", puede ser 🟡. Como está, dudoso.

010 🟡🔄 - "Cómo clonar tu disco viejo a un SSD nuevo sin perder nada" — el "sin perder nada" es el miedo del viewer, está más cerca. Reformulación: "Migré al SSD nuevo y perdí todo. El error que nadie te avisa." — gira desde el miedo a la consecuencia real, activa curiosity gap con conocimiento parcial previo (el viewer ya sabe que se puede clonar, no sabe que puede fallar).

011 🟠❌ - "Guía definitiva AM5: armá tu PC para el futuro" — "guía definitiva" es título de tutorial educativo largo, no de contenido viral de 47s. El ángulo "para el futuro" es vago. Podría funcionar como YouTube evergreen, no como Reel viral. Formato A incompatible por scope.

---

### 9. Versus (Agente 5 — segunda mitad)

001 🟡🔄 - "Air Cooling vs Liquid Cooling" — comparación sin conflicto personal del viewer. Cien canales grandes lo tienen. Reformulación: "Me convencieron de comprar un AIO y fue una cagada. Lo que no te dicen los que lo recomiendan." — el conflicto tiene que ser del viewer que ya tomó la decisión equivocada.

002 🟡🔄 - "SSD SATA vs NVMe para gaming" — tema con confusión real (el viewer creyó que NVMe = más FPS). Curiosity gap activable porque el viewer YA tiene uno de los dos. Reformulación: "Pagué el doble por NVMe pensando que iba a subir los FPS. No cambió nada." — twist contra-intuitivo confirmado por métricas reales del audit (hook score patrón = 8-9/10 cuando hay expectativa frustrada).

003 🟠🔄 - "Intel vs AMD en 2025 ¿quién gana en precio-rendimiento?" — mega-saturado, Nate Gentile y todos los canales grandes lo actualizan cada 6 meses. Regla del audit: "si el tema ya lo hizo un canal grande, descartá". El viewer no tiene un conflicto personal activo sobre esto salvo que esté por comprar. Dudoso salvo que haya un ángulo específico del mercado argentino/MdP que justifique el punto de vista local.

004 🔴❌ - "Monitor IPS vs VA vs TN" — trivia técnica sin conflicto. El viewer que no está por comprar no le importa. El que está por comprar ya lo buscó. Sin primera persona, sin situación de conflicto activo. Tutorial lineal de specs.

005 🔴❌ - "750W vs 850W de fuente" — trivia sin conflicto. Ningún viewer tiene un problema activo con la potencia de su fuente. Sin tensión, sin twist posible. Genera saves de "referencia", no shares.

006 🟠🔄 - "DDR4 vs DDR5" — hay confusión real del viewer (especialmente en contexto AM5 donde DDR5 es obligatorio) pero como está formulado es tutorial de specs. Curiosity gap activable solo si hay un twist de precio/rendimiento contra-intuitivo. Necesita más contexto: en combinación con idea 011 (AM5) podría tener ángulo, standalone es dudoso.

007 🟡🔄 - "Windows 10 vs Windows 11 para gaming en 2025" — hay un conflicto real del viewer que se niega a actualizar y no sabe si está perdiendo FPS. Curiosity gap presente (YA tiene W10 o W11, YA juega). Reformulación: "Seguí en Windows 10 todo el año. Cuando migré a 11 pasó algo que no esperaba." — la sorpresa tiene que ser concreta (mejor, peor, igual) y el twist tiene que ser contra-intuitivo para el debate que el viewer ya tiene en la cabeza.

008 🔴❌ - "Disco externo vs NAS vs nube" — trivia sin conflicto personal. Tres opciones técnicas sin situación de primer persona. El viewer no tiene un drama activo sobre esto. Tutorial comparativo lineal.

009 🔴❌ - "Teclado mecánico vs membrana" — trivia sin conflicto. Sin drama personal activo del viewer. El que ya decidió no le importa. El que no decidió lo busca en Google, no en un Reel de 47s.

010 🔴❌ - "Cooler de stock vs cooler aftermarket" — tutorial sin tensión. Sin conflicto del viewer, sin primera persona, sin consecuencia real mencionada en el título. El ángulo "cuántos grados de diferencia" es educativo, no viral.

---

## Ideas ya ejecutadas — análisis post-mortem

### ✅ QWERTY fue diseñado para que escribas MÁS LENTO — VIRAL

- **Resultado real**: VIRAL (confirmado en 07_IDEAS_POOL.md y en audit de Agente 3).
- **Patrón que cumple**: el viewer usa el teclado todos los días + twist fuerte (está diseñado en tu contra) + gap preexistente con el objeto + altamente WhatsApp-able. Cumple los 3 filtros del audit: conflicto del viewer, tiene twist no lineal, se manda por WhatsApp.
- **Aprendizaje**: los datos curiosos solo funcionan cuando el objeto del dato es algo que el viewer ya usa a diario. Si no hay relación previa del viewer con el objeto, no hay gap posible.

---

### ✅ Desactivá la Xbox Game Bar si no la usás — VIRAL (240K views)

- **Resultado real**: 240K views, citado en audit como ejemplo canónico de tip con conflicto envuelto.
- **Patrón que cumple**: tip puro transformado en conflicto del viewer con conclusión equivocada (Windows graba en background sin que el viewer lo sepa = pérdida de FPS activa). La causa es oculta, la consecuencia es medible, el viewer lo manda al amigo que se queja de FPS bajos.
- **Aprendizaje**: cualquier tip puede funcionar si el conflicto del viewer se pone antes que la solución. El tip es la resolución, nunca el hook.

---

### ✅ 1 Gbps de internet ≠ 100 MB/s (bits vs bytes) — VIRAL

- **Resultado real**: hook score 8/10 en audit, mencionado como patrón válido en múltiples agentes.
- **Patrón que cumple**: primera persona del viewer que paga por algo ("contrato 1GB"), causa oculta (conversión bits/bytes), twist verificable con dato concreto. Mismo esquema que el ISP cagando (idea #9 del bloque directo a cámara).
- **Aprendizaje**: el gancho de injusticia económica personal ("pago X y recibo Y") es el patrón más reproducible del banco. Se puede aplicar a RAM, SSD, plan de internet, antivirus, sillas gamer.

---

### ✅ Standoffs / separadores de motherboard (gabinete da patada eléctrica) — validado

- **Resultado real**: validado como Formato B (no tiene métricas en el audit pero está citado como ejemplo de conclusión equivocada perfecta).
- **Patrón que cumple**: conclusión equivocada con acción inminente (el gabinete está defectuoso = devolución inminente), causa oculta no obvia (standoffs faltantes = cortocircuito), diagnóstico progresivo natural para Formato B.
- **Aprendizaje**: las ideas con causa oculta que el viewer jamás hubiera adivinado solo son Formato B nativo. Llevarlas a Formato A pierde la tensión del diagnóstico.

---

### ✅ Cables de fuente vieja en fuente nueva — validado como Formato B

- **Resultado real**: validado empíricamente según Agente 1.
- **Patrón que cumple**: conclusión equivocada con riesgo real (cables no universales entre marcas = componentes quemados). Resistencia activa del principiante que defiende su decisión.
- **Aprendizaje**: las ideas con riesgo real de daño a componentes caros son naturalmente WhatsApp-ables porque el viewer manda el video a alguien que está por cometer el mismo error.

---

### ❌ PS3 supercomputadora — FLOP (3/10 hook score)

- **Resultado real**: 3/10 hook score, citado en audit como ejemplo canónico de "trivia sin conflicto".
- **Patrón que falló**: el viewer no tenía ningún problema activo relacionado con los superordenadores del ejército ni con la PS3. Sin gap previo activado, no hay curiosity gap posible. El dato es curioso pero no genera tensión ni acción.
- **Aprendizaje**: un dato puede ser impactante y aun así no funcionar si el viewer no tiene ninguna relación previa activa con el tema. La sorpresa sola no es suficiente — necesita un gap que el viewer ya tenía abierto.

---

### ❌ DLSS 5 reaction — FLOP (4/10 hook score)

- **Resultado real**: 4/10 hook score, validado como patrón flop "reacción a contenido externo".
- **Patrón que falló**: asume que el viewer vio el video original de DLSS 5, que conoce el debate interno del nicho y que viene con contexto previo del canal. Audiencias solapadas = casi nunca se cumple la suposición.
- **Aprendizaje**: cualquier video que empiece con "¿viste ese video de...?" o "hay gente que dice que..." está asumiendo audiencias solapadas. Eso es una apuesta perdedora según el audit.

---

### ✅ "No es tan difícil ¿vieron?" — VIRAL ABSOLUTO (3.97M views, 42K shares)

- **Resultado real**: mayor viral de la cuenta. 3.97M views en IG, 42K shares, 115K likes.
- **Patrón que cumple**: no hay datos del formato en el audit, pero el título sugiere identificación social con arquetipo universal + tono deadpan que desmonta una barrera de entrada. Posiblemente Formato C o Formato B con arquetipo.
- **Aprendizaje**: el mayor viral de la cuenta tiene el hook de "esto no es tan difícil como creés" — desmonta una barrera de entrada para la audiencia. Vale la pena analizar el guion completo para detectar el patrón exacto replicable.

---

## Recomendaciones operativas

### 1. Patrones repetidos en las 🔴 (qué patrones flop dominan cada categoría)

- **PRO vs PRINCIPIANTE**: ideas sin conclusión equivocada activa ni acción inminente. El principiante solo describe un síntoma sin tomar ninguna decisión incorrecta = no hay tensión narrativa (ideas 050, 054, 059).
- **Directo a cámara**: preguntas abiertas del creador ("¿cuándo conviene?", "¿vale la pena?") en lugar de conflicto activo del viewer. Genera tutoriales de consulta que se guardan pero no se comparten (ideas 015, 024).
- **Mitos tech**: correcciones de trivia sin consecuencia práctica activa. El mito es incorrecto pero nadie tiene una decisión bloqueada por creerlo ahora mismo (ideas 010, 014, 017, 020).
- **Datos curiosos**: trivia sin gap preexistente del viewer con el objeto del dato. 15 de 25 son datos de almanaque sin ningún puente hacia el viewer actual (ideas 001, 002, 003, 008, 009, 012, 013, 017, 019, 021, 023).
- **Tips**: instrucciones puras sin conflicto envolvente. El patrón Xbox Game Bar (lo que funciona) es la excepción, no la regla (ideas 002, 005, 006, 008, 010, 011, 017, 019).
- **Storytime arreglo**: historias de clientes en tercera persona donde el conflicto es del creador que observa, no del viewer que se identifica (ideas 004, 007, 012, 020).
- **Tutoriales y Versus**: estructuralmente incompatibles con formato viral de 47s. El patrón flop es universal en estas dos categorías.

---

### 2. Categorías a priorizar para Formato A (las 3 con mayor densidad 🟢⭐)

**1. Mitos tech** — 8 ideas 🟢⭐ de 20 procesadas (40% de conversión). Las mejores del banco para Formato A puro: creencia activa + twist con consecuencia práctica + dato verificable = fórmula limpia. Próximo mes: grabar al menos 4 de las 8 ideas 🟢⭐ del bloque.

**2. Directo a cámara** — 10 ideas 🟢⭐ de 30 procesadas (33% de conversión). La categoría con más volumen de 🟢⭐ en términos absolutos. El problema es de formulación (preguntas abiertas), no de tema. Las que ya tienen la formulación correcta son grabables esta semana.

**3. Storytime ensamble** — 5 ideas 🟢 de 16 procesadas (31% combinando ⭐ y 🔄). La categoría de storytime de ensamble tiene el mayor potencial de virales emocionales (Le armé la PC a mi viejo, PC de 500 USD para pibe de 15). Formato A en modo Storytelling, no Explicativo.

---

### 3. Categorías casi exclusivas para B o C (las que no funcionan a cámara)

- **Tutoriales** (11 ideas): 0% de conversión a Formato A. Todas requieren demostración visual paso a paso. Formato correcto: YouTube evergreen largo (> 10 min) o contenido de curso, no Reels de 47s.
- **PRO vs PRINCIPIANTE** (60 ideas): el 70% tiene conflicto activado, pero el valor está en el diálogo de diagnóstico. 18 son incompatibles con Formato A porque el twist depende del intercambio verbal. Categoría nativa del Formato B.
- **Storytime arreglo**: 9 de 22 ideas requieren B-roll del hardware para que el impacto exista. Sin imágenes, el story pierde el 60% de su valor. No son ideas de Formato A salvo las 5 que se pueden contar como anécdota pura (005, 013, 014, y con reformulación: 001, 006).

---

### 4. Top 5 ideas para reformular ya (las 🟡 con más potencial y reformulación más fácil)

**1. A1-035 — "Compré RAM de 4800MHz y corre a 2400"**
Reformulación: "Pagué por RAM de 4800MHz. El BIOS la tenía limitada a 2400 desde fábrica." — mismo patrón que el viral de bits/bytes, XMP no activado, el conflicto está en la compra ya hecha. Un cambio de formulación la convierte en 🟢⭐.

**2. A2D-003 — "Por qué las GPUs usadas de minería no dan tanto miedo"**
Reformulación: "Te dijeron que una GPU de minería te iba a durar dos meses. Mentira." — activa la creencia antes de desmontarla. La contra-narrativa tiene potencial alto porque va contra el consenso del nicho.

**3. A4S1-015 — "Rescatando los datos de un HDD que hace click"**
Reformulación: "Tu HDD hace click. Eso significa que tenés X horas para hacer esto antes de perderlo todo." — transforma el story en urgencia del viewer, primera persona implícita, curiosity gap activo.

**4. A5V-002 — "SSD SATA vs NVMe para gaming"**
Reformulación: "Pagué el doble por el NVMe convencido de que iba a subir los FPS. Cero diferencia." — twist contra-intuitivo, expectativa frustrada, patrón validado en el audit con hook score 8-9/10.

**5. A4S2-005 — "Mi primera PC: todos los errores que cometí"**
Reformulación: "Los errores que cometés cuando armás tu primera PC. Y que nadie te avisa." — traslada la primera persona del creador al viewer, activa identificación en toda la audiencia que armó PC o está por armar.

---

## Patrones cruzados detectados

**Patrón 1: "Compré X y me da Y" es la fórmula más rentable del banco.**
Detectado por Agentes 1 y 3, confirmado por resultados reales. Las ideas que tienen esta estructura son sistemáticamente las de mayor curiosity gap: RAM de 4800MHz que corre a 2400 (A1-035), 100 megas que bajan a 2 MBs (A1-020 viral), NVMe que no sube los FPS (A5-002). El conflicto es siempre entre lo que el viewer pagó y lo que obtiene. Categorías afectadas: PRO vs PRINCIPIANTE, Mitos tech, Versus.

**Patrón 2: Las ideas de tercera persona son consistentemente más débiles que las de primera.**
Detectado por Agentes 3, 4 y 5 de forma independiente. En storytime arreglo, el 70% de las ideas están formuladas como "el cliente que X" — conflicto del creador que observa, no del viewer. En datos curiosos, las que están en tercera persona histórica (Ada Lovelace, ENIAC, el primer mouse) son todas 🔴. Las que tienen al viewer como sujeto activo (QWERTY viral, JPG destruye tu imagen, USB-C son iguales) son todas 🟢. La reformulación más simple y más efectiva del banco es trasladar el sujeto de la oración del creador/tercero al viewer.

**Patrón 3: El gancho de injusticia económica es el segundo más fuerte después del conflicto de primera persona.**
Detectado por Agentes 1, 2 y 4. Ideas con estructura "te están robando plata sin que lo sepas": ISP cagando (A2D-009), antivirus pago en 2025 (A2M-003), GPU de segunda en Argentina vs USA (A4S2-008), plan Balanced baja FPS (A2M-013). Todas son 🟢⭐. El audit lo confirma con el viral de bits vs bytes (hook 8/10 = exactamente ese patrón). Categorías con mayor concentración: Mitos tech y Directo a cámara.

**Patrón 4: Los tutoriales y el Versus son categorías estructuralmente incompatibles con el formato viral de 47s.**
Detectado de forma independiente por Agentes 3 y 5, con confirmación empírica en el audit (Tip para limpiar PC, 2/10; tutoriales = saves, no shares). Las 11 ideas de Tutoriales y las 10 de Versus tienen 0 clasificaciones 🟢. Esto no implica que los temas sean malos — implica que el formato de Reel de 47s es el vehículo equivocado. La solución no es reformular estas ideas para Reels sino moverlas a YouTube como contenido evergreen largo.

**Patrón 5: El thermal cluster (pasta térmica, ventiladores, cooler, orientación de fans) tiene alta superposición temática.**
Detectado solo por Agente 1 pero con implicaciones para todo el banco. Las ideas A1-003, A1-005, A1-016, A1-017, A1-056 abordan variaciones del mismo problema (thermal management por error del usuario). Publicarlas en ventana cercana las canibaliza. La recomendación es elegir las dos con mayor impacto visual y diferencia de causa (005: pasta desbordada y 016: plástico en el cooler) y relegar las demás a pipeline de largo plazo.
