# Investigación — Referencias y patrones para la Memoria 2025 de HLA

Fecha: 2026-06-22. Investigación de referencias de memorias anuales interactivas, patrones
de UX/UI, recomendaciones técnicas y tendencias de diseño.

> Nota: `countrast.com` es una SPA; no se pudo extraer su UI concreta. Se trata su patrón
> (clic en dato → gráfico de evolución) como brief objetivo, no como hecho verificado.

## 1. Referencias para enseñar al cliente

### Sector salud
- **Cleveland Clinic — Annual Report.** La referencia del sector: cifras del año + historias
  de paciente. El dato frío se humaniza con narrativa. → Aplicable directamente a HLA.
  (my.clevelandclinic.org/about/overview/financial-information)
- **Mayo Clinic.** Reporting anual con fuerte marca institucional sanitaria.
- **NIHCM Data-Driven Storytelling Award.** Premio anual que recopila las mejores
  visualizaciones de datos del sector salud → cantera de ejemplos premiados.

### Informes corporativos con storytelling de datos
- **Adidas Annual Report 2024.** Scrollytelling modular: informe árido convertido en historia
  navegable por bloques con elemento visual que cambia al scroll. → **Es exactamente el
  "elemento central que cambia por sección".**
- **B Lab 2023.** Clic en elementos/gráficos/texto para explorar al instante. → Lo más
  cercano al patrón Countrast (dato clicable que despliega profundidad).
- **AstraZeneca.** Scroll largo, mucho espacio en blanco, color audaz, stats que "saltan".
  Sector farma/salud, premium. → KPIs que respiran (encaja con "elegante y sencillo").
- **Gates Foundation.** Narrativa de impacto con datos (referencia para comunicar valor
  asistencial, no solo financiero).

### Galerías / premios para seguir explorando
ARC Awards (Interactive Annual Report) · Maglr (best scrollytelling) · scrollytelling.ai ·
Vev (annual reports) · DataComms Awards · Online Journalism Awards · Posit Closeread Prize.

## 2. Patrones de UX/UI recomendados

**Núcleo (encajan con el brief):**
1. **Big Number / stat counter animado** — número grande + frase corta; cuenta al entrar
   en viewport (no al cargar).
2. **Drill-down / click-to-expand a histórico** — KPI clicable que despliega *in situ*
   (no navega) el gráfico de 3 años. Affordance clara (cursor, icono "+", microanimación
   al hover). Expandir en su sitio (acordeón/card que crece o drawer ligero).
3. **Elemento central sticky (scrollytelling)** — elemento visual fijo que se transforma
   mientras avanza el texto. Patrón estructural principal (estilo Adidas Year in Review).

**Navegación:**
4. **Tabs/secciones sticky + scroll** — nav superior con anclas (Asistencia, Calidad,
   Investigación, Sostenibilidad, Cifras…) + scroll vertical dentro de cada sección.
5. **Bento grid** en la portada/resumen de KPIs — celdas de distinto tamaño, cada una un
   big number clicable. Tendencia 2025.

**Motion:**
6. Scroll-triggered reveals (fade-in/slide-up sutil).
7. Transición animada (altura+opacidad, spring) al expandir el gráfico.

**Arquitectura propuesta:** portada bento de KPIs → secciones temáticas con scrollytelling
de elemento central sticky → KPIs con drill-down a histórico de 3 años.

## 3. Recomendaciones técnicas

| Decisión | Recomendación | Por qué |
|----------|---------------|---------|
| Gráficos | **Recharts** | Estándar React 2025, SVG, integra con shadcn/ui, ~50KB. Perfecto para series cortas. Alternativa: **visx** si se quiere identidad muy propia. |
| Animación nº | **Motion `AnimateNumber`** | Spring physics, dispara al entrar en viewport. Alternativa ligera: `react-countup`. |
| Reveals/expand | **Motion** | `whileInView`, `AnimatePresence` para montar/desmontar el gráfico animado. |
| Stack sitio | **React + Vite (Lovable)** | Microsite, despliegue trivial (Vercel), carga rápida. |
| Datos | **Supabase** | El cliente quiere editar cifras cada año vía backoffice → fuente gobernada, no JSON estático. |

**Accesibilidad técnica:** tabla de datos accesible alternativa al SVG · drill-down
operable por teclado (`aria-expanded`, foco) · `prefers-reduced-motion` · contraste AA (AAA
en texto crítico).

## 4. Tendencias de diseño 2024–2025

- **Bento grids** para organizar datos heterogéneos.
- **Tipografía expresiva** (serifs con carácter, variable fonts) + **kinetic typography**.
- **Motion como identidad** (sutil, no efectista).
- **Color con presencia / alto contraste** (elegante sin ser tímido).
- **Accesibilidad holística** (especialmente reputacional en salud).
- **Abandono del PDF estático** → experiencias web interactivas.

## Síntesis accionable

1. Estructura: scrollytelling con elemento central sticky + bento grid de KPIs en portada.
2. Interacción estrella: KPI clicable → expande gráfico de 3 años in situ, con affordance
   clara y transición animada.
3. Stack: React + Vite + Supabase (backoffice editable).
4. Librerías: Recharts + Motion.
5. Estética: bento, serif expresiva, motion sutil, color alto contraste, accesibilidad AA/AAA.
