# Decisiones — HLA · Memoria Anual 2025

> Registro de decisiones técnicas y de producto. Añadir entradas con fecha.

## 2026-06-22 — Arranque del proyecto

- **Stack:** React + Vite + Supabase (datos + backoffice). Se descarta JSON estático
  porque el cliente quiere editar cifras/textos cada año sin desarrollador.
- **Gráficos:** Recharts (suficiente para series de 3 puntos, integra con React, ligero).
- **Animación:** Motion / Framer Motion.
- **Patrón UX:** portada tipo bento grid + big numbers animados + drill-down in situ +
  elemento central sticky (scrollytelling).
- **Equipo:** Cristian + cliente directamente. Facturable. ~95h.

## 2026-07-27 — Dirección de diseño v5 (post-auditoría vs. Countrast)

Auditoría completa en [`auditoria-y-plan-diseno-v5.md`](auditoria-y-plan-diseno-v5.md).
Decisiones confirmadas por Rebeca:

- **D1 · Fondo papel neutro `#F4F3F1`** sustituye al blanco azulado `#FBFAFE`. *Revisado el
  27-jul:* la propuesta inicial era un crema `#F5F3EE`, pero la paleta oficial de HLA es
  fría (violeta, gris azulado, azul, verde agua, magenta) y el crema amarillea el rosa. El
  papel neutro conserva el carácter editorial sin pelearse con los cinco colores de marca.
- **D2 · Antonio 400 para las cifras KPI** + **IBM Plex Mono** para toda la fontanería del
  dato (eyebrows, captions en mayúsculas, ejes, unidades, etiquetas de valor, deltas).
  Antonio es display condensada: excelente a 70px, ilegible a 11px — por eso la mono no
  compite con ella, la complementa. *Reparto: Antonio dice la cifra, Plex Mono la explica,
  Poppins la cuenta.*
- **D3 · Titulares en Antonio 500** (`line-height .92`). Antonio es la tipográfica de marca
  según indicación de Rebeca (27-jul); sustituye a la propuesta inicial de Poppins 500/600.
  Verificada: variable 100–700, subsets latin + latin-ext, cubre acentos, ñ, ¿, € y ↑↓−.
  **Ojo: es condensada — la misma cifra ocupa ~35 % menos ancho que Poppins 900, así que la
  métrica de la rejilla se rehace, no se escala.**
- **D4 · Rosa de marca `#CF0C71` como acento secundario** = serie histórica, frente a
  violeta `#4D418A` = año actual. **Cierra la decisión abierta del color de acento:** el
  rojo de los mockups del cliente se legitima como segunda serie de datos, no como alarma.
  *Revisado el 27-jul:* sustituye a la propuesta de terracota `#C4532B` al recibirse la
  carta de color oficial. El rosa además encaja mejor con la lógica de la referencia
  —saturación altísima en superficie mínima, igual que su naranja y su cian—.
- **D10 · Paleta oficial de HLA con reparto de papeles.** Cinco colores, ninguno decorativo:
  violeta `#4D418A` (dato actual, elemento central), rosa `#CF0C71` (serie histórica),
  gris `#63666F` (texto secundario), azul `#639AB7` (tercera serie), agua `#A8D3CE`
  (rellenos). **Azul y agua nunca llevan texto encima** (2,6:1 y 1,5:1 sobre papel).
  Contrastes verificados: violeta 7,8:1 AAA · rosa 4,8:1 AA · gris 5,9:1 AA · blanco sobre
  violeta 8,6:1 AAA · blanco sobre rosa 5,3:1 AA.
  Sustituye a los valores que se habían derivado del PNG del isotipo (`#52428C`, `#5E51A0`).
- **D5 · Fuera las píldoras verde/rojo de delta.** El semáforo de dashboard no encaja en una
  memoria institucional de salud (menos urgencias no es "malo"). El delta pasa a mono
  discreto y, cuando aplica, lo cuenta el propio gráfico.
- **D6 · `border-radius: 0` y cero sombras en todo el sitio.** La estructura la construyen
  hairlines de 1px y el aire, no contenedores. Es el rasgo más definitorio de la referencia.
- **D7 · Sin fotografía.** Todo el peso recae en tipografía y dato.
- **D8 · El histórico se abre transformando el elemento central**, no en una tarjeta aparte
  (brief de Vicky). El modelo que ya tenía la v4 es el correcto; solo cambia su ejecución.
- **D9 · Hairlines de conexión** entre el elemento central y los indicadores que lo rodean,
  tal como aparecen en los wireframes del cliente. La v4 los había perdido.

## 2026-07-27 (tarde) — Iteración v5.1 sobre feedback de Rebeca

- **D11 · Full-bleed.** Fuera el `max-width: 1280px`: la página usa todo el ancho, como la
  referencia. Padding lateral fluido `clamp(28px, 4vw, 72px)`. El nav distribuye las 7
  pestañas + logo con `space-between` a lo ancho. Más separación centro ↔ KPIs
  (`gap: clamp(56px, 7vw, 130px)`), cifras más grandes, centro más grande (580px) — **el
  contenedor central es el protagonista**.
- **D12 · Poppins ELIMINADA — sistema de dos voces.** La prosa no casaba con la mono.
  Todo el texto corrido pasa a **IBM Plex Mono** (13–14px / 1.7), y los subtítulos pequeños
  en bold (Hitos, etc.) pasan a **Antonio 500 en mayúsculas**. Es la fórmula exacta de
  Countrast (Rubik + Reddit Mono). Resuelve de paso la duda de la prosa: ya no hay tercera
  familia. Pendiente solo validar con el manual de marca cuando llegue.
- **D13 · Cada sección editorial tiene su visual de sistema** (mientras llega el contenido
  real del cliente, que sigue pendiente — las secciones llevan 3 datos reales de la Memoria
  2023 como placeholder):
  - *Hitos / Innovación* → *rail*: espina hairline con nodos huecos, índice mono, cifra
    Antonio violeta gigante.
  - *Sociedad* → matriz de 50 puntos (6 en violeta = hospitales HLA en el ranking MRS).
  - *Personas* → pulso ECG animado (segmento violeta viajando sobre trazado fantasma).
  - *Cliente* → barra de proporción: 28 % pacientes nuevos sobre el total (dato derivado
    real: 298.595 / 1.048.207).
  - *Sostenibilidad* → anillo 99 % renovable con barrido animado y el 1 % como hueco.
- **D14 · Gráficas animadas.** El histórico se dibuja al abrirse: leader lines en fade
  escalonado, trazo de línea (`pathLength`), puntos con pop, etiquetas con rise, count-up
  en la cifra grande. Todos los visuales de sección animan a la entrada (stagger).
  **Todo dentro de `@media (prefers-reduced-motion: no-preference)`** — con motion
  reducido, los estados finales se muestran directamente.

Principio rector heredado de la referencia: **el dato nunca va solo** — siempre con unidad,
definición en micro-caption y, cuando haya datos por centro, su posición dentro de la
distribución del conjunto.

**Nota:** la referencia **no usa degradados** en su UI (solo en los renders 3D de los
globos). Su carácter premium viene de contención, densidad de dato y voz tipográfica. Se
reserva un único degradado sutil para el elemento central sticky.

## Decisiones abiertas

- [x] ~~**Color de acento:** rojo (mockups) vs azul marino (web actual).~~ → Resuelto en D4:
      violeta HLA (actual) + terracota (histórico).
- [ ] Secciones definitivas y qué KPIs llevan histórico.
- [ ] Multi-idioma sí/no.
- [ ] Origen de los datos históricos (3 años).
- [ ] **Datos desglosados por centro** — habilitan el gráfico de distribución (la
      interacción estrella, §6 del plan). Petición prioritaria al cliente.
- [ ] ¿Montamos las fundaciones en Figma antes de código, o código primero y Figma como
      entregable? (recomendación: código primero, la pieza es muy tipográfica).
