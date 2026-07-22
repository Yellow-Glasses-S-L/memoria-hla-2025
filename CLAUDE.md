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
- **Color (CONFIRMADO desde grupohla.com):** marca **violeta/púrpura** sobre **blanco**,
  titulares en **azul índigo oscuro**, paneles **lavanda**. Paleta del mockup:
  bg `#FBFAFE` · ink `#2A2657` · acento violeta `#5E51A0` · lavanda `#F1EEF9`.
  El ROJO de los mockups del cliente era solo color de relleno del boceto, NO de marca.
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

## Tipografía y marca aplicadas (mockup)
- Fuente: **Poppins** (la real de HLA; DIN es la secundaria propietaria). Embebida en el mockup.
- Logo: isotipo oficial `https://www.grupohla.com/assets/isotipo.png` (anillo violeta) embebido como data URI.
- Violeta de marca exacto del isotipo: `#52428C`.

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
