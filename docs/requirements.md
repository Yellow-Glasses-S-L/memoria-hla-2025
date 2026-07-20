# Requisitos — HLA · Memoria Anual 2025

## Contexto

HLA necesita renovar el formato de su Memoria Anual. La versión actual
(<https://memoria.grupohla.com/>) presenta KPIs en tarjetas, pero el cliente quiere algo
más cuidado y dinámico, inspirándose en <https://countrast.com/> para la interacción de
"clic en el dato → gráfico de evolución histórica".

## Objetivo

Un microsite **agradable, sencillo y dinámico**, estéticamente muy cuidado, con los colores
y términos de la marca HLA.

## Requisitos funcionales

1. **Navegación por pestañas/secciones.** El elemento central cambia según cada
   sección. Algunas secciones muestran solo cifras; otras combinan números con textos,
   hitos o titulares.
2. **Mensajes cortos y directos.** Cada KPI lleva un número grande y una frase breve.
3. **Drill-down al histórico.** En los indicadores con evolución temporal, al pinchar el
   elemento (rojo en los mockups) se abre un gráfico con la evolución de los últimos 3 años.
4. **Animación.** Contadores que cuentan al entrar en viewport; transiciones suaves al
   expandir el gráfico; elemento central sticky que se transforma con el scroll.
5. **Backoffice sencillo.** El cliente debe poder editar las cifras, textos y secciones
   cada año, y ajustar algo de diseño/estructura, sin rehacer el sitio.

## Requisitos no funcionales

- **Estética premium**, coherente con la marca HLA.
- **Responsive** (móvil, tablet, desktop).
- **Accesibilidad** AA/AAA (teclado, `prefers-reduced-motion`, contraste, alternativa
  textual a gráficos). Crítico por ser sector salud.
- **Performance** (carga rápida, microsite ligero).
- **Reutilizable cada año** (gobernanza del dato vía backoffice).

## Fuera de alcance (por ahora)

- Multi-idioma (a confirmar con cliente).
- Integraciones con sistemas internos de HLA (los datos se cargan vía backoffice).

## Stack confirmado

React + Vite (front) · Supabase (datos + backoffice) · Recharts (gráficos) ·
Motion/Framer Motion (animación) · Vercel (deploy).

## Decisiones pendientes

- Color de acento: ¿**rojo** (mockups) o **azul marino** (web actual)?
- Lista definitiva de secciones y de qué KPIs llevan histórico.
- ¿Multi-idioma?
- Origen y formato de los datos históricos de los últimos 3 años.
