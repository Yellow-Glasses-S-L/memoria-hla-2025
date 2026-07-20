# Plan de milestones y tareas — HLA · Memoria Anual 2025

Budget total: ~95h (5.700 min). Todas las tareas facturables, asignadas a Cristian.

## M1 · Discovery, contenido y diseño — 2026-07-11 (~26h)

| Tarea | Est. |
|-------|------|
| Kick-off + recopilación de cifras de la memoria con cliente | 3h |
| Arquitectura de secciones + KPIs con histórico + modelo de datos anual | 3h |
| Moodboard + dirección de arte (marca HLA) | 4h |
| Diseño UI del microsite en Figma (portada + secciones + drill-down) | 12h |
| Diseño del backoffice sencillo (pantallas de edición) | 2h |
| Revisión y aprobación del diseño con cliente | 2h |

## M2 · Datos y backoffice (Supabase) — 2026-07-25 (~16h)

| Tarea | Est. |
|-------|------|
| Setup Supabase (proyecto, schema KPIs/secciones/series, RLS) | 5h |
| Seed de datos 2025 + históricos | 2h |
| Backoffice CRUD (cifras, textos y secciones editables) | 8h |
| Auth básica del backoffice | 1h |

## M3 · Build del microsite — 2026-08-15 (~37h)

| Tarea | Est. |
|-------|------|
| Setup proyecto React+Vite + conexión a Supabase | 3h |
| Portada bento + navegación sticky por secciones | 8h |
| Componente Big Number animado (count-up en viewport) | 4h |
| Drill-down: gráfico evolución 3 años (Recharts) + expand animado | 8h |
| Scrollytelling / elemento central sticky por sección | 8h |
| Responsive + accesibilidad (teclado, prefers-reduced-motion, contraste) | 6h |

## M4 · Contenido, QA y entrega — 2026-08-29 (~13h)

| Tarea | Est. |
|-------|------|
| Carga de contenidos reales + revisión de cifras | 4h |
| QA cross-browser + performance | 3h |
| Ajustes finales tras feedback del cliente | 4h |
| Despliegue (Vercel + Supabase prod) + subdominio grupohla | 2h |
