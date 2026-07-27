# Auditoría de diseño y plan de elevación — Memoria HLA 2025 · v5

Fecha: 2026-07-27 · Autor: Yellow Glasses (dirección de diseño)
Base auditada: `mockup/memoria-hla-v4.html` (= `index.html`, versión de Cristian)
Referencia: <https://countrast.com/fi/al?unit=imperial&sort=lifeExpectancy>
Nueva versión de trabajo: `mockup/memoria-hla-v5.html`

---

## 1. Método

No se ha juzgado "a ojo". Se ha inspeccionado la referencia en navegador extrayendo sus
valores computados reales (fuentes cargadas, colores, grosores, `stroke-dasharray`,
paddings, `letter-spacing`, `line-height`) y se ha hecho lo mismo con nuestra v4. Los
tokens de la sección 3 son medidos, no estimados.

---

## 2. Auditoría de la v4 — qué falla

### 2.1 Bugs (no son opinión de diseño, están rotos)

| # | Problema | Detalle |
|---|----------|---------|
| B1 | **Sin `<meta charset>`** | El fichero es UTF-8 pero no tiene `<!doctype>`, `<html>` ni `<head>`. El navegador cae a `windows-1252` y **rompe todos los acentos**: "InnovaciÃ³n", "CirugÃ­as", "DiagnÃ³stico", "aÃ±o". Visible en toda la web. *Ya corregido en la v5.* |
| B2 | **Solape en "Hitos"** | La columna del número tiene ancho fijo; con "+15M€" el número se monta encima del texto contiguo. |
| B3 | **Etiquetas recortadas en el drill-down** | Los valores de la serie ("981.416", "1.048.207") se salen de la tarjeta y quedan cortados por el borde. |
| B4 | **Badge flotante solapando el footer** | "MOCKUP · DATOS 2023" pisa el texto del pie. |
| B5 | **Media página vacía en varias secciones** | "Hitos" ocupa el tercio superior y deja ~450 px muertos. No hay ritmo vertical. |

### 2.2 Diseño — por qué "se ve IA"

Esto es lo importante. La v4 no es fea; es **genérica**. Y es genérica por razones
concretas y corregibles:

1. **Todo son tarjetas redondeadas con sombra.** 13 elementos con `border-radius: 20px`,
   más `10px`, `8px`, `30px`, `50%` — cinco radios distintos sin sistema. La referencia
   tiene **`border-radius: 0px` en absolutamente todo**. El "card con esquinas blandas y
   sombra difusa" es la firma visual del template de dashboard.
2. **Píldoras verde/rojo de delta.** `↑1,4% vs 2024` en verde menta y `↓−2,2%` en rosa es
   semáforo de dashboard de SaaS. Es el elemento más "plantilla" de toda la página y en una
   memoria institucional de salud además chirría (verde/rojo = bueno/malo, y menos urgencias
   no es "malo").
3. **Una sola familia tipográfica en pesos extremos.** Poppins al 800/900 para titulares y
   cifras. Poppins Black es, probablemente, la tipografía más asociada al "landing generada
   por IA". Además geométrica + muy pesada = ruidoso, no premium.
4. **Los números no tienen voz propia.** Son texto en negrita del mismo tipo que el resto.
   Sin cifras tabulares, sin alineación, sin tratamiento de dato.
5. **Cero estructura visible.** No hay una sola línea fina que ordene la página. La
   composición se sostiene solo por espacios en blanco mal repartidos → sensación de
   flotar.
6. **El elemento central tiene el modelo correcto pero la ejecución plana.** El mecanismo
   está bien resuelto —el bloque central dice "pincha un indicador" y al hacerlo se
   convierte en el gráfico histórico, que es exactamente lo que pide Vicky (§2.4)—. Lo que
   falla es la forma: un rectángulo violeta con esquinas blandas y sombra, **sin las líneas
   finas de conexión** a los indicadores de alrededor que sí aparecen en los wireframes del
   cliente. Sin esos hairlines el elemento central no se lee como el centro de nada: es una
   tarjeta más flotando en medio.
7. **Fondo azulado frío** (`#FBFAFE`). Lee a producto digital. Tanto la referencia
   (`#F4F3EC`) como los wireframes del cliente usan un **blanco cálido de papel**, que es
   lo que da el aire editorial de memoria anual.
8. **Los datos aparecen solos.** Un número grande sin contexto no informa. La referencia
   nunca enseña un dato sin situarlo: siempre lleva unidad, definición y **su posición
   dentro del conjunto**.

### 2.3 Lo que la v4 sí hace bien y hay que conservar

- La arquitectura de 7 secciones (Indicadores, Hitos, Sociedad, Personas, Cliente,
  Sostenibilidad, Innovación) es correcta y coincide con los wireframes del cliente.
- **El modelo de interacción es el correcto**: el histórico se abre *en el elemento
  central*, no en una tarjeta aparte. Coincide con lo que pide Vicky. Se conserva tal cual;
  solo cambia su ejecución visual.
- El drill-down funciona y es accesible por teclado (`aria-label` en los botones KPI).
- La decisión de violeta HLA sobre claro es correcta y está bien extraída de la marca
  (`#52428C` es el violeta real del isotipo). **La paleta no se toca en su núcleo.**
- Poppins es la tipográfica de marca: se mantiene, pero cambia de rol (ver §5.2).

### 2.4 El brief de Vicky (correo a Cristian) — fuente de verdad

Cinco instrucciones literales del cliente, que mandan sobre cualquier interpretación nuestra:

1. El **elemento central va cambiando** según cada pestaña/sección.
2. Algunos apartados llevan **solo cifras**; otros **combinan números con textos, hitos o
   titulares**.
3. Los mensajes son siempre **cortos y directos**.
4. **Desde el elemento rojo (= el central) se abre el histórico** cuando el indicador tiene
   evolución temporal. El histórico no se abre en una tarjeta aparte: **el centro se
   transforma**.
5. Lo que le interesa de Countrast es concretamente **que al pinchar un dato se abra el
   gráfico de los últimos tres años**.

Los wireframes acompañantes añaden dos cosas que no están en el texto pero se ven: **fondo
blanco cálido** y **líneas finas que conectan el elemento central con los indicadores**.
Ambas se incorporan al sistema (§5.1 y §5.4).

Lectura de diseño: lo que Vicky pide como "elemento central que cambia" es, en realidad,
**un escenario único y persistente**. No es un contenedor que muestra cosas distintas; es
el protagonista de la página, y todo lo demás orbita a su alrededor conectado por
hairlines. Esa es la diferencia entre la v4 (tarjeta en medio) y la v5 (centro de gravedad).

---

## 3. El ADN de la referencia (valores medidos)

```
Fondo papel        #F4F3EC   (rgb 244,243,236) — cálido, no blanco
Tinta              #050505   (casi negro, nunca #000 puro en texto grande)
Masa de datos      #C5C9C1   (gris cálido verdoso, relleno del área)
Líneas / grid      #C4C4C2   1px, dasharray 8 8
Texto secundario   #A19E91   (gris cálido, no gris azulado)
Acento A           #FF5601   (naranja)
Acento B           #00BFFF   (cian)

Tipografía         Reddit Mono 400  → TODO el dato, cifras, ejes, captions
                   Rubik 500        → solo nombres propios / display
line-height        1.0   (16px/16px, 14px/14px — muy compacto)
letter-spacing     −0.02em  (−0.32px sobre 16px)
border-radius      0px      en todos y cada uno de los elementos
box-shadow         ninguna
degradados         ninguno en la UI (solo el render 3D del globo)
```

**Etiqueta de valor (el componente estrella):**
rectángulo sólido de acento, `padding: 4px 6px`, `radius: 0`, texto blanco mono 16px/16px
con sublabel minúscula debajo, anclado al punto con una **línea vertical de 1px** que
recorre toda la altura del gráfico, y un **círculo hueco** (relleno blanco, borde 1px del
acento) exactamente sobre el dato.

### 3.1 Los cinco principios que hacen que funcione

1. **Planitud radical.** Sin radios, sin sombras, sin degradados, sin tarjetas. La
   estructura la construyen **líneas de 1px y el aire**, no contenedores.
2. **El dato nunca va solo.** Siempre lleva unidad, definición en micro-caption y —lo
   decisivo— **su posición dentro de la distribución completa**. La silueta gris no es
   decoración: son los 190 países ordenados, y tu dato está clavado ahí dentro.
3. **El color es un puntero, no decoración.** El 95% de la superficie es papel y grises.
   El color solo aparece sobre los valores que se están comparando, en superficie mínima.
4. **Voz monoespaciada para el dato.** El mono comunica precisión e instrumento de medida,
   y regala alineación tabular. Es el 90% de por qué se ve "de autor" y no de plantilla.
5. **Micro-etiquetas rigurosas.** Bajo cada cifra, una caption de 11-12px en mayúsculas
   espaciadas que dice exactamente qué es y en qué unidad.

---

## 4. Qué copiamos y qué NO

Copiar la referencia entera sería un error. Countrast es una **herramienta** de
comparación en viewport fijo (su página literalmente no hace scroll: 900px de alto). La
Memoria HLA es un **relato** con scroll y secciones. Tomamos su lenguaje visual y de
datos, no su arquitectura de aplicación.

| Sí adoptamos | No adoptamos |
|---|---|
| Planitud total: radius 0, sin sombras | El viewport fijo sin scroll |
| Voz mono para todo el dato | Su paleta (naranja/cian) |
| Hairlines de 1px como estructura | El layout de comparación A vs B |
| Etiquetas ancladas con línea guía | El selector de países |
| Fondo papel cálido | La densidad de UI de herramienta |
| El dato dentro de su distribución | — |
| Micro-captions en mayúsculas | — |

**Nota honesta sobre los degradados:** me pediste que me fijara en ellos, y el hallazgo es
que **la referencia no tiene degradados en la UI**. Lo único degradado son los renders 3D
de los globos terráqueos. Su sensación premium no viene de degradados: viene de
contención, densidad de dato y voz tipográfica. Mi recomendación es no meter degradados
salvo en **un solo sitio**: el elemento central sticky, tratado como objeto atmosférico
(un gris muy sutil que le dé volumen, como el globo). Si metemos degradados en tarjetas y
fondos, perdemos exactamente lo que queremos ganar.

---

## 5. Sistema de diseño propuesto para la v5

### 5.1 Color — paleta oficial de marca

> Actualizado 2026-07-27 con la carta de color oficial de HLA. Sustituye a los valores
> que se habían derivado del PNG del isotipo.

```css
/* ---- PALETA OFICIAL HLA ---- */
--violeta  #4D418A   /* 77/65/138  · CMYK 82/86/0/4  — principal */
--gris     #63666F   /* 99/102/111 · CMYK 57/46/40/25 */
--azul     #639AB7   /* 99/154/183 · CMYK 61/20/14/5 */
--agua     #A8D3CE   /* 185/216/202 · CMYK 33/0/20/0 */
--rosa     #CF0C71   /* 207/12/113 · CMYK 1/100/14/3 */

/* ---- neutros derivados ---- */
--paper    #F4F3F1   /* papel neutro */
--paper-2  #EAE9E6   /* banda alterna / fondo del elemento central */
--ink      #1F1D2B   /* casi negro con matiz violeta */
--line     #DDDCD9   /* hairline 1px */
--mass     #C7C8CB   /* relleno "el resto del conjunto" en distribuciones */
```

**Reparto de papeles** — cada color tiene una función, ninguno es decorativo:

| Color | Función | Contraste sobre papel |
|-------|---------|----------------------|
| Violeta `#4D418A` | Dato actual (2025) · elemento central · titular destacado | **7,8:1 — AAA** |
| Rosa `#CF0C71` | Serie histórica · el dato comparado · affordance de "abre histórico" | **4,8:1 — AA** |
| Gris `#63666F` | Texto secundario · captions · eyebrows | **5,9:1 — AA** |
| Azul `#639AB7` | Tercera serie · acento de sección | 2,6:1 — **solo superficie, nunca texto** |
| Agua `#A8D3CE` | Rellenos de área · bandas de fondo | 1,5:1 — **solo superficie, nunca texto** |

Blanco sobre violeta = 8,6:1 (AAA). Blanco sobre rosa = 5,3:1 (AA) — suficiente para las
etiquetas de valor. Azul y agua **no pueden llevar texto encima**: quedan reservados a
superficie.

**Rosa en vez de terracota.** El rosa de marca `#CF0C71` sustituye a la propuesta anterior
y funciona mejor: es exactamente la lógica de la referencia —saturación muy alta en
superficie mínima— igual que su naranja `#FF5601` y su cian `#00BFFF`. Sigue resolviendo la
decisión pendiente del "rojo" del cliente: no como alarma, sino como **segunda serie de
datos**.

**El papel deja de ser crema.** La paleta de HLA es fría (violeta, gris azulado, azul,
verde agua, magenta) y un fondo crema amarillea el rosa. Se pasa a un **papel neutro
`#F4F3F1`**: conserva el carácter de papel sin pelearse con los cinco colores de marca.
Comparativa de tres opciones en el bloque 01 del specimen — la diferencia es sutil por
muestra, pero se acumula a lo largo de una página entera.

⚠️ **Inconsistencia detectada:** el SVG del logo viene en `#4D4084` y la carta de color
dice `#4D418A`. Diferencia imperceptible pero real. Se toma **`#4D418A`** como token (manda
la carta de color) y se sirve el logo recoloreado. Confirmar si se prefiere al revés.

### 5.2 Tipografía — sistema de tres voces

> Revisado 2026-07-27 tras indicación de Rebeca: **Antonio** (Google Fonts) es la
> tipográfica de marca y va en **titulares y números**.

Sistema de tres papeles, cada uno con una función estricta:

| Rol | Fuente | Peso | Tamaño | Tracking |
|-----|--------|------|--------|----------|
| **Display de sección** | **Antonio** | 500 | 56–80px | −0.01em, `line-height .92` |
| **Cifras KPI** | **Antonio** | **400** | 72–120px | −0.005em, `tabular-nums`, `lh .86` |
| Cuerpo / prosa | Poppins | 400 | 16–18px | −0.01em |
| Captions, ejes, eyebrows | IBM Plex Mono | 400 | 10–12px | +0.10/+0.14em, mayúsculas |
| Etiquetas de valor | IBM Plex Mono | 400 | 14px + 10px sublabel | −0.02em |
| Deltas y unidades | IBM Plex Mono | 400 | 11px | +0.04em |

**Antonio (verificada en Google Fonts):** variable 100–700, subsets `latin` + `latin-ext`.
Cubre acentos, ñ, ü, ¿ y € sin problema, y además trae ↑ ↓ − en el subset latin, que es
justo lo que necesitan los deltas. Probada con las cifras reales de HLA en
`mockup/specimen-antonio.html`.

Tres hallazgos del specimen:

1. **Peso 400 es el punto.** 200/300 son elegantes pero pierden presencia a tamaño grande;
   **700 es demasiado** y devuelve el aire de "cartel" que queremos evitar. Titulares a 500,
   cifras a 400.
2. **Antonio es condensada: la misma cifra ocupa ~35 % menos de ancho que en Poppins 900.**
   Es una ventaja enorme para el big number —permite cifras mucho mayores en el mismo
   espacio— pero **obliga a rehacer la métrica de la rejilla**. No vale escalar la v4.
3. Sus cifras son de ancho uniforme, así que las columnas de datos alinean solas.

**La mono sigue siendo necesaria, y no compite con Antonio.** Antonio es una display
condensada: excelente a 70px, ilegible a 11px. Toda la "fontanería" del dato —eyebrows,
captions en mayúsculas, ejes, unidades, etiquetas de valor, deltas— necesita una voz de
instrumento de precisión, y ahí es donde vive el rigor de la referencia. IBM Plex Mono se
queda en ese papel, siempre pequeña y en mayúsculas o tabular.

Reparto final, en una frase: **Antonio dice la cifra, Plex Mono la explica, Poppins la
cuenta.**

⚠️ **Contradicción a resolver:** `CLAUDE.md` registra que la tipográfica de HLA es Poppins
("la real de HLA; DIN es la secundaria propietaria") y ahora la indicación es Antonio.
Aplicamos Antonio en titulares y cifras según lo indicado, y **Poppins se mantiene en la
prosa** a falta del manual de marca (material 3 de §8). Conviene confirmarlo con el cliente
antes de F5.

### 5.3 Estructura

- Rejilla de 12 columnas con **gutters visibles en hairline**, no invisible.
- Ritmo vertical base 8px. Altura mínima de sección coherente (se acaban los huecos de 450px).
- Patrón de cabecera de sección: eyebrow mono en mayúsculas + título Poppins 500 +
  **regla de 1px a todo el ancho** debajo.
- Cero tarjetas. Los bloques se separan con líneas, no con cajas.

### 5.4 Componentes a especificar

1. **`KpiFigure`** — eyebrow mono / cifra mono grande / caption mayúsculas / delta discreto
   (mono, sin píldora, sin color semáforo).
2. **`ValueTag`** — la etiqueta de la referencia: rect sólido radius 0, padding 4/6, valor
   + sublabel, línea guía de 1px y círculo hueco sobre el dato.
3. **`DistributionChart`** — silueta gris del conjunto ordenado con los valores destacados
   clavados encima. **Es la interacción estrella** (ver §6).
4. **`HistorySeries`** — el drill-down de 3 años: línea 1.5px violeta, puntos huecos, grid
   discontinuo 6/6, ejes en mono, sin tarjeta contenedora.
5. **`CenterObject`** — el elemento central sticky que muta por sección, **conectado por
   hairlines a los KPIs de alrededor** (recuperando el wireframe del cliente).
6. **`SectionHeader`**, **`Hairline`**, **`TabNav`** (sin píldora rellena; subrayado fino).

---

## 6. La idea que puede hacer notable esta memoria

El verdadero hallazgo de Countrast no es estético, es conceptual: **enseña un dato dentro
de su distribución completa**. No dice "esperanza de vida 79,1"; dice "79,1, y aquí está
ese 79,1 entre los 190 países del mundo".

El equivalente para HLA es directo y potente: HLA tiene **una red de centros**. En vez de
"ocupación hospitalaria 52,1%", enseñar la silueta de **todos los centros HLA ordenados**
con los destacados clavados encima. Lo mismo con pacientes por centro, cirugías por centro,
urgencias por centro.

Eso convierte una cifra corporativa plana en un objeto explorable y honesto, y además da
sentido real al drill-down y al hover. **Es la diferencia entre una memoria bonita y una
memoria que alguien quiere recorrer.** Para esto necesito el dato desglosado por centro
(§8, material 2) — es la petición más importante de la lista.

Y el elemento central sticky: propongo que sea un **sistema de anillos/arcos** que
reconfigura por sección (distribución → línea temporal → mapa de centros → anillo). El
isotipo de HLA ya es un anillo, así que el objeto central sería marca y dato a la vez.

---

## 7. Plan de trabajo

Todo sobre `mockup/memoria-hla-v5.html`. `index.html` sigue apuntando a la v4, así que el
deploy de Vercel no se rompe mientras trabajamos. Al cerrar la v5, se repunta.

| Fase | Trabajo | Estado (27-jul) |
|------|---------|--------|
| **F0 · Saneado** | doctype + `<meta charset>` + viewport | ✅ Hecho |
| **F1 · Fundaciones** | Tokens (paleta oficial), Antonio + Plex Mono + Poppins, radius 0, hairlines, ritmo | ✅ Hecho — v5 reescrita desde cero |
| **F2 · Componentes de dato** | `KpiFigure`, `ValueTag`, `HistorySeries`. Sin píldoras. B2 B3 B4 arreglados | ✅ Hecho |
| **F3 · Elemento central** | Centro con isotipo rotando + **conectores hairline dibujados por JS** (se realinean con ResizeObserver, el del KPI activo se enciende en rosa) + el centro **se transforma** en el histórico (D8) | ✅ Hecho (falta morphing por sección, ver F5+) |
| **F4 · Distribución** | `DistributionChart` con datos por centro | ⏸ Bloqueado — falta el dato por centro (material ⭐) |
| **F5 · Resto de secciones** | Sistema aplicado a las 7 secciones. B5 resuelto | ✅ Primera pasada hecha |
| **F6 · Movimiento** | Count-up en viewport ✅, transform del centro ✅, reveals ✅, `prefers-reduced-motion` ✅. Falta: scrollytelling del elemento central, morphing entre secciones | 🔶 Parcial |
| **F7 · Responsive + A11y** | Móvil ✅ (stack, centro primero), teclado ✅ (Escape, foco gestionado, `aria-expanded`, `aria-live`), contrastes AA/AAA ✅. Falta: tabla de datos alternativa, tablet fino | 🔶 Parcial |

**Verificado en navegador (27-jul):** sin colisiones de etiquetas en ningún dataset
(probado pico-en-medio con Urgencias), tags dentro de límites en 390px, Escape cierra y
devuelve el foco al KPI que abrió, hairlines de 1px reales (`vector-effect`), puntos
circulares (HTML, no SVG escalado). Capturas en `auditoria-v5/v5-*.png`.

**Detalles de implementación que conviene conservar en el build React:**
- Conectores: SVG overlay recalculado por `ResizeObserver`, línea del KPI activo → rosa.
- Etiquetas de valor: HTML posicionado (no SVG) para texto nítido; ancla derecha-de-línea
  el primer año, izquierda-de-línea el resto → geometría sin colisiones para 3 puntos.
- Logo e isotipo vía `mask` CSS + `background: var(--violeta)` → temables por token.
- Isotipo del centro: rotación 80s linear (se desactiva con `prefers-reduced-motion`).

---

## 8. Materiales que necesito de ti

Ordenados por impacto en la calidad final:

1. **Datos reales 2025 + histórico 2023-2024-2025** por KPI, en hoja de cálculo. Indicando
   **qué KPIs tienen histórico y cuáles no** — condiciona qué es clicable.
2. **⭐ Desglose por centro.** Aunque sean 2-3 métricas de cada uno de los ~40 centros.
   Es lo que habilita la interacción de la §6, la que puede hacer notable la pieza. Si solo
   consigues un material de esta lista, que sea este.
3. **Manual de marca HLA** (PDF). Con la carta de color ya resuelta, queda la duda
   tipográfica: ¿manda Antonio también en la prosa, o se queda Poppins? ¿DIN sigue siendo
   secundaria? Si no hay manual, dime quién decide en el cliente.
4. ~~**Logo e isotipo en SVG.**~~ ✅ **Recibido 27-jul** → `mockup/assets/hla-logo.svg`.
   Queda por pedir el **isotipo suelto** (solo el anillo, sin wordmark): es lo que permitiría
   que el elemento central sea el propio anillo de HLA recoloreado y animado.
5. **La Memoria 2024 (y 2023) en PDF.** Para estructura real de contenidos, secciones
   oficiales y tono editorial. Evita que inventemos secciones que luego no existen.
6. **Fotografía de HLA en alta** (centros, equipos, quirófanos) — o confirmación de que
   **no** va a haber fotografía. Cambia la dirección de diseño radicalmente: sin foto, todo
   el peso recae en tipografía y dato; con foto, hay que diseñar la convivencia. Necesito
   saberlo antes de F1.
7. **Textos**: carta del consejero, titulares de sección y los "mensajes cortos" que
   acompañan a cada KPI. Si aún no existen, un par de ejemplos del tono me valen para
   maquetar con longitudes reales en vez de lorem.
8. **Otras referencias** que te gusten a ti o al cliente, aunque sean de otros sectores.
   Y si el cliente ha dicho algo sobre qué le gusta de countrast, mejor: quiero saber si le
   atrae el minimalismo o la interacción.

Sobre Figma: en `CLAUDE.md` figura como pendiente. Dime si quieres que montemos ahí las
fundaciones (tokens + componentes) antes de código, o si tiramos directo a código en la v5
y luego documentamos. Para una pieza tan tipográfica, mi opinión es que **iterar en código
es más rápido** y Figma después como entregable.

---

## 9. Decisiones — CONFIRMADAS 2026-07-27

| # | Decisión | Estado |
|---|----------|--------|
| D1 | Fondo **papel neutro `#F4F3F1`** (revisado: el crema amarilleaba el rosa de marca) | ✅ Revisado 27-jul |
| D2 | **Antonio 400 para las cifras KPI** · IBM Plex Mono para captions, ejes, etiquetas y deltas | ✅ Revisado 27-jul |
| D3 | **Titulares en Antonio 500** (antes: Poppins 500/600) | ✅ Revisado 27-jul |
| D4 | **Rosa de marca `#CF0C71`** como serie histórica — cierra el "¿rojo?" pendiente | ✅ Revisado 27-jul |
| D5 | Eliminar píldoras verde/rojo de delta | ✅ Confirmado |
| D6 | Radius 0 y cero sombras en todo el sitio | ✅ Confirmado |
| D7 | Sin fotografía — el peso recae en tipografía y dato | ✅ Confirmado |
| D8 | El histórico se abre **transformando el elemento central** (brief de Vicky) | ✅ Confirmado |
| D9 | Hairlines de conexión centro ↔ indicadores (wireframes del cliente) | ✅ Confirmado |

Registro en [`decisions.md`](decisions.md). Validación visual en
`mockup/specimen-antonio.html`. **F1 desbloqueada.**

Pendiente de confirmar con cliente (no bloquea): qué tipografía manda en la **prosa**, dada
la contradicción Poppins/Antonio de §5.2.
