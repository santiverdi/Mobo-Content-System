# 12 — FORMATO G: ADS META (paid social)

> Formato pago. NO es contenido orgánico. Reglas distintas: CTA explícito, hook califica audiencia rápido, métrica de éxito es CPA/ROAS (no shares).
> La voz de marca MOBO se mantiene (rioplatense, filosa, primera persona) pero la arquitectura cambia: problema → agitación → solución → CTA.

---

## Sub-modelos

El Formato G se divide en dos sub-modelos según objetivo de campaña:

- **G-Volume** — generar mensajes baratos para venta de componentes sueltos (GPU, RAM, SSD). Ticket bajo, ciclo corto.
- **G-Ticket** — generar leads calificados para PCs armadas. Ticket alto, ciclo más largo (lead → presupuesto → visita al local → cierre).

<!-- VERIFICAR: estructura final de creatividades por sub-modelo (hook + body + CTA) — pendiente sistematizar a partir de las campañas que sí rindieron -->

---

## Status de validación (mayo 2026, post-cruce con database real)

**Data conocida:**
- 10 campañas corridas Mar-May 2026
- $1.57M ARS gastados (~$784K ARS abril)
- 2,532 mensajes generados
- Database de ventas abril cruzada con campañas

**Hallazgo crítico mayo 2026**: la intuición original de "20% de mensajes
convierten en venta" estaba SOBREESTIMADA 20-25x. La realidad medida es:

- 11 ventas Web en abril (canal único atribuible a digital)
- ~1,265 mensajes generados por ads en abril
- Conversión real: **~0.9% mensaje → venta Web atribuida**
- ROAS neto realista: **2.5-3x** (no 26x como sugería la intuición)

**MUY IMPORTANTE — caveat de atribución**: el sistema de POS de MOBO
solo tiene 2 canales: Presencial y Web. Las PCs armadas que se cierran
en el local pero originaron desde ads de WhatsApp se cargan como
Presencial. **El ROAS real puede ser hasta 3x mayor que el medido**,
pero no es trazable hasta que se implemente el campo "origen del lead"
en el POS.

**Implicancia operativa**: las campañas son rentables al ras (2.5x ROAS
neto) si solo se cuenta lo trazable. Probablemente más rentables,
pero no medible. NO son la "máquina de oro" que la intuición sugería.

**Mejor campaña por costo/mensaje**: VB - Compra Placas V → $273/msj
**Peor campaña por costo/mensaje**: VB - WhatsApp PC - Copia → $2,202/msj

---

## Sub-modelo G-Volume

Objetivo: mensajes a WhatsApp para componentes sueltos (típicamente GPU).
Ticket promedio observado: USD $300. Ciclo de cierre: corto (mismo día / 24h).
Hook tipo: "compra X" / "placa de video desde $Y" — directo, sin curiosity gap largo.
CTA: "mandanos mensaje" / link a WhatsApp Business.

<!-- VERIFICAR: lista final de creatividades G-Volume validadas y sus métricas individuales -->

**Validado en abril 2026**: las 9 GPUs sueltas vendidas por Web tuvieron
ticket promedio de USD $300 y margen del 41%. La campaña VB - Compra
Placas V (apagada en abril por cap de presupuesto) probablemente alimentaba
la mayoría de estas ventas. **Reactivar prioridad alta.**

---

## Sub-modelo G-Ticket

Objetivo: leads calificados para PCs armadas a medida.
Ticket promedio observado: USD $800-1,500. Ciclo de cierre: largo (lead → presupuesto → visita al local → cierre presencial).
Hook tipo: problema del viewer ("PC para Fortnite sin gastar de más", "qué PC me armo con X plata") — más cerca del orgánico, pero con CTA explícito.
CTA: "te armamos el presupuesto" / "vení al local".

<!-- VERIFICAR: estructura tipo de creatividad G-Ticket que rindió mejor -->

**Hallazgo crítico abril 2026**: las 20 PCs armadas vendidas en abril
representan el 57% de la facturación y 53% del margen total del mes
(USD $5,303 de margen). **TODAS se cargaron como Presencial**, pero
muchas probablemente vinieron de ads de WhatsApp (lead → presupuesto →
visita al local → venta).

**Implicancia**: el ROAS de las campañas G-Ticket está SUBESTIMADO en
el sistema actual. La campaña "VB - WhatsApp PC" (cara: $1,379/msj)
puede ser la más rentable del conjunto si los presupuestos efectivos
se cierran al venir al local. **No medible sin campo de origen en POS.**

---

## ⚠️ DEUDA TÉCNICA EXPLÍCITA

Este Formato G está construido sobre **3 hechos validados (mayo 2026)**
+ **1 deuda técnica crítica**:

**Validado**:
1. Conversión mensaje → venta es ~0.9% (no 20%). ROAS neto realista
   2.5-3x.
2. Las "Copias" rinden peor que originales sistemáticamente.
3. PC armadas son el 53% del margen total del negocio. Casi todas
   se cierran Presencial.

**Deuda técnica crítica que invalida cualquier optimización fina**:
- POS de MOBO solo tiene 2 canales (Presencial / Web)
- Imposible saber qué % de las ventas Presencial vinieron originalmente
  de ads
- **Acción correctiva urgente**: agregar campo "origen del lead" al
  POS con opciones: Ad IG/FB, Recomendación, Búsqueda Google, Walk-in,
  Cliente recurrente. Obligatorio al cargar venta.

Mientras tanto: las campañas son rentables al ras pero no se puede
optimizar individualmente cuál performa mejor.
