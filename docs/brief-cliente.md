# Brief del cliente — Memoria HLA 2025

Fuente primaria del encargo. Manda sobre cualquier interpretación nuestra.

---

## Correo de Vicky (HLA) a Cristian

> Hola Cris, ¿cómo estás?
>
> Te paso lo que comentamos recién sobre la landing de la Memoria de HLA.
>
> Landing actual: https://memoria.grupohla.com/
>
> Referencia de nueva landing: https://countrast.com/fi/al?unit=imperial
>
> Me parece interesante de esta referencia que, **al pinchar en algunos datos, se abre el
> gráfico con la evolución histórica de los últimos tres años**.
>
> Te dejo abajo unos mockups bastante básicos 😅 para explicar la idea:
>
> - El **elemento central iría cambiando** según cada pestaña/sección.
> - Algunos apartados tendrían **solo cifras** y otros combinarían **números con textos,
>   hitos o titulares**.
> - La idea es que los **mensajes sean siempre cortos y directos**.
> - **Desde ese elemento rojo se abriría el histórico** cuando se trate de indicadores o
>   datos que tengan evolución temporal.
>
> Lo vemos cuando puedas 😊
>
> ¡¡¡Mil gracias!!!
>
> Un abrazo,
> Vicky

## Wireframes adjuntos

En [`../Referencias/`](../Referencias/). Dos pantallas con la misma estructura:

- Nav superior de 7 secciones con el logo HLA centrado.
- **4 indicadores alrededor de un elemento central** (el rectángulo rojo).
- **Líneas finas conectando el elemento central con los indicadores** — 2 a cada lado.
- Variante A: 4 KPIs simétricos. Variante B: 1 KPI grande + 3 bloques de texto numerados
  (el caso "números + textos/hitos").
- Cada cifra lleva **eyebrow arriba** (fecha/periodo) y **caption en mayúsculas debajo**.
- Fondo **blanco cálido**, no blanco puro.

⚠️ El **rojo del rectángulo es color de relleno del boceto**, no color de marca. Confirmado
en `CLAUDE.md`. Se reinterpreta como acento secundario terracota para la serie histórica
(ver D4 en [`decisions.md`](decisions.md)).

## Cómo se traduce al diseño

| Lo que pide Vicky | Cómo se resuelve | Dónde |
|---|---|---|
| Elemento central que cambia por sección | `CenterObject` sticky, escenario único y persistente | Plan §5.4, F3 |
| Histórico al pinchar un dato | El centro **se transforma** en el gráfico (no tarjeta aparte) | D8, F2 |
| Mensajes cortos y directos | Cifra Antonio + caption mono en mayúsculas, sin prosa alrededor | §5.2 |
| Secciones solo-cifras vs. mixtas | Dos plantillas de sección sobre la misma rejilla | F5 |
| Líneas de conexión (wireframe) | Hairlines de 1px centro ↔ indicadores | D9, F3 |
| Fondo cálido (wireframe) | `--paper #F5F3EE` | D1, F1 |

## Indicaciones de marca (Rebeca, 2026-07-27)

- **Antonio** (Google Fonts) es la tipográfica de marca → **titulares y números**.
  Ver §5.2 del plan y la contradicción pendiente con Poppins en la prosa.
- **Carta de color oficial** recibida — 5 colores. Ver §5.1 del plan y la tabla de marca en
  `CLAUDE.md`. Sustituye a los valores que se habían derivado del PNG del isotipo.
- **Logo oficial en SVG** recibido → `mockup/assets/hla-logo.svg`.

## Material recibido

- [x] **Logo HLA en SVG** — 27-jul. Lockup completo, vectorial, monocromo `#4D4084`.
- [x] **Carta de color de marca** — 27-jul. 5 colores con CMYK/RGB/HEX.
- [x] **Wireframes del cliente** — en `../Referencias/`.
- [x] **Brief de Vicky** — arriba.

## Material pendiente

- [ ] **⭐ Desglose por centro** — habilita el gráfico de distribución (§6 del plan).
- [ ] Datos 2025 + histórico 3 años, indicando qué KPIs tienen serie.
- [ ] Manual de marca (resolvería la duda Poppins/Antonio en prosa).
- [ ] Memoria 2024 en PDF — estructura real de contenidos.
- [ ] Textos: carta del consejero, titulares, mensajes cortos de cada KPI.
- [ ] Resto en §8 del [plan](auditoria-y-plan-diseno-v5.md).
