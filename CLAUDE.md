# HLA · Memoria Anual 2025 — Landing interactiva

> Microsite de la Memoria Anual de HLA: elegante, sencillo y dinámico. KPIs de mensaje
> corto con drill-down al histórico de 3 años (clic en indicador → gráfico de evolución).

## Datos del proyecto

- **PEX_PROJECT_ID:** `74b0e1df-9ed7-41d8-8148-f93bee305eaf`
- **Cliente:** HLA · Salud (`1443141e-885a-4cdd-bbe8-d2a63280590d`)
- **Comercial / Responsable:** Cristian Hoyos (`74ab56b3-2144-4b22-9bec-6c7ea193e3b9`)
- **Equipo:** lo desarrollan Cristian + cliente directamente
- **Facturable:** Sí · **Budget:** ~95h (5.700 min)
- **Inicio:** 2026-06-22 · **Entrega estimada:** 2026-08-29

## Objetivo

Microsite de la Memoria 2025 de HLA con dos ideas fuerza:

1. **KPIs de mensaje corto y directo** — número grande + frase breve. Cuenta hacia arriba
   al entrar en pantalla.
2. **Drill-down al histórico** — al pinchar un indicador con evolución temporal, se
   despliega *in situ* un gráfico con los últimos 3 años (interacción estilo Countrast).
3. **Elemento central que cambia por sección** — scrollytelling con elemento visual sticky
   que se transforma al avanzar.

Referencia web actual: <https://memoria.grupohla.com/>
Referencia de interacción: <https://countrast.com/fi/al?unit=imperial>

## Stack

- **Frontend:** React + Vite (vía Lovable)
- **Datos + backoffice:** Supabase (PostgreSQL + Auth + RLS). El cliente debe poder
  **editar cifras/textos cada año** y ajustar algo de diseño/estructura desde un
  **backoffice sencillo**. ⚠️ NO usar JSON estático.
- **Gráficos:** Recharts (series cortas, SVG, integra con React)
- **Animación:** Motion / Framer Motion (`AnimateNumber` para contadores;
  `whileInView` + `AnimatePresence` para reveals y expand del gráfico)
- **Deploy:** Vercel (front) + Supabase prod. Subdominio en `grupohla.com`.

## Marca

- **Lema:** "Medicina, Experiencia, Personas"
- **Paleta OFICIAL** (carta de color del cliente, 2026-07-27 — manda sobre cualquier valor
  derivado de capturas o del PNG del isotipo):

  | Color | HEX | RGB | CMYK | Papel en la memoria |
  |-------|-----|-----|------|---------------------|
  | Violeta | `#4D418A` | 77/65/138 | 82/86/0/4 | Principal · dato actual · elemento central |
  | Gris | `#63666F` | 99/102/111 | 57/46/40/25 | Texto secundario · captions |
  | Azul | `#639AB7` | 99/154/183 | 61/20/14/5 | Tercera serie · solo superficie |
  | Verde agua | `#A8D3CE` | 185/216/202 | 33/0/20/0 | Rellenos · solo superficie |
  | Rosa | `#CF0C71` | 207/12/113 | 1/100/14/3 | Serie histórica · comparación |

  Neutros derivados: papel `#F4F3F1` · papel-2 `#EAE9E6` · ink `#1F1D2B` · line `#DDDCD9`.
  ⚠️ Azul y verde agua **nunca llevan texto encima** (2,6:1 y 1,5:1 sobre papel).
  ⚠️ El SVG del logo viene en `#4D4084`; manda la carta de color, `#4D418A`.
  El ROJO de los mockups del cliente era relleno del boceto: se reinterpreta como el rosa
  de marca para la serie histórica.
- **Valores obsoletos** (derivados del PNG, ya NO usar): `#52428C`, `#5E51A0`, `#FBFAFE`,
  `#2A2657`, `#F1EEF9`.
- **Secciones de referencia:** Carta Consejero · Quiénes somos · Cuidado de las personas ·
  Innovación · Equipo HLA · ESG

## KPIs de referencia (Memoria 2023, magnitud orientativa)

| KPI | 2023 |
|-----|------|
| Urgencias | 579.430 |
| Ingresos | 76.600 |
| Citas en consultas externas | 3.276.538 |
| Cirugías | 163.892 |
| Pruebas de diagnóstico | 730.839 |
| Pacientes atendidos | 1.048.207 |
| Ocupación hospitalaria | 52,1 % |
| Crecimiento facturación | 2,94 % |

## Accesibilidad (no opcional — sector salud)

- Operable por teclado (drill-down con `aria-expanded`, foco gestionado al expandir)
- Respetar `prefers-reduced-motion` (desactivar count-up y reveals)
- Contraste AA mínimo, AAA en texto crítico
- Alternativa textual / tabla de datos accesible para los gráficos SVG

## Milestones

| # | Milestone | Fecha | ID |
|---|-----------|-------|----|
| M1 | Discovery, contenido y diseño | 2026-07-11 | `d4ce849e-2826-4045-ad89-f813e7755602` |
| M2 | Datos y backoffice (Supabase) | 2026-07-25 | `29f3effa-4d9d-47cc-a1ab-f5d2992429e4` |
| M3 | Build del microsite | 2026-08-15 | `d207ae09-6902-4734-8995-dab71df4ba4d` |
| M4 | Contenido, QA y entrega | 2026-08-29 | `65c3b268-5a74-421b-a614-7f719dc203dd` |

## Entornos (rellenar cuando existan)

- Supabase DEV: _pendiente_
- Supabase PROD: _pendiente_
- Repo GitHub: https://github.com/Yellow-Glasses-S-L/memoria-hla-2025 (org Yellow-Glasses-S-L, público)
- URL despliegue (mockup): https://memoria-hla-2025.vercel.app (Vercel, **team `yellow-glasses`** — propiedad de empresa, transferido desde la cuenta personal el 2026-07-22; proyecto memoria-hla-2025, público). Objetivo final: subdominio grupohla.com
- Figma: _pendiente_

## Tipografía y assets

**Sistema de DOS voces (v5.1, decidido 2026-07-27 tarde — Poppins ELIMINADA):**
- **Antonio** (Google Fonts, variable 100–700) → **titulares (500), cifras (400) y
  subtítulos pequeños en mayúsculas (500, ~21px)**. Es la tipográfica de marca; el wordmark
  del logo es una condensada casi idéntica. ⚠️ Es **condensada**: ~35 % menos ancho que una
  sans normal — la rejilla se diseña para ella.
- **IBM Plex Mono** → **todo lo demás, incluida la prosa** (13–14px / 1.7–1.8): eyebrows,
  captions, ejes, etiquetas de valor, deltas, párrafos, footer. Es la fórmula exacta de la
  referencia Countrast (Rubik display + Reddit Mono para todo).
- ~~Poppins~~ eliminada del sistema: no casaba con la mono. Ya no se carga.

*Reparto en una frase: Antonio dice la cifra, Plex Mono cuenta todo lo demás.*

**Assets:**
- Logo oficial en SVG: `mockup/assets/hla-logo.svg` (lockup isotipo + HLA + Grupo
  Hospitalario, 142×34, monocromo). Versión temable:
  `mockup/assets/hla-logo-currentcolor.svg`.
  ⚠️ La versión `currentColor` **debe inlinearse en el HTML**; cargada vía `<img>` no
  hereda el color y sale negra.
- Ya NO usar el PNG del isotipo incrustado como data-URI de la v4.

## Deploy (auto-deploy por git — desde 2026-07-20)
El proyecto Vercel `memoria-hla-2025` (team **`yellow-glasses`**) está **conectado al repo GitHub**: cada push a `main`
dispara un deploy a producción. `vercel.json` hace rewrite `/ → mockup/index.html` (el
mockup vive en `mockup/`, no en la raíz). Verificado: push → deploy Ready → `memoria-hla-2025.vercel.app` HTTP 200.
- `vercel` desde local: usar `--scope yellow-glasses` (el `.vercel/` local se re-enlazó tras la transferencia).
- Cuando llegue el build React/Vite: mover el output a la raíz (o ajustar el rewrite / Root Directory) y quitar el `vercel.json` del mockup.
- Método antiguo (ya no usar): CLI `vercel deploy --prod` desde carpeta aislada. NO usar el MCP `deploy_to_vercel` (despliega el CWD, con material de otros clientes).

## Pendientes de arranque

- [ ] Recibir y revisar carpeta **"Referencias"** del cliente (mockups + imágenes) — aún no sincronizada
- [ ] Confirmar **rojo** como color de acento del drill-down
- [ ] Kick-off con cliente + recopilación de cifras 2025 y de los 3 años de histórico
- [ ] Configurar MCPs del proyecto (Supabase, GitHub, Notion, Figma) en `.claude/settings.json`
