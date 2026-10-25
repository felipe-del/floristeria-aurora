# Floristería Aurora — Proyecto 2 (EIF-511 Arquitectura de Información)

Tienda en línea de **flores (tema 7: Floristería)** hecha con **Nuxt 3**, con carrito de compras **Snipcart** y comentarios **Utterances**.

APP: https://floristeria-aurora.netlify.app/

## Requisitos del enunciado y dónde se cumplen

| Requisito | Implementación |
|---|---|
| Catálogo de ≥ 30 artículos | `data/articulos.json` (38 artículos) |
| Info genérica + específica | Genérica: `nombre`, `descripcion`, `categoria`, `imagen`, `etiquetas`. Específica: `precio`, `tamano`, `color`, `ocasion`, `contenido` |
| Listas de categorías | `data/categorias.json` (6 categorías) |
| Documentos JSON que generan el sitio | Las páginas se construyen desde esos JSON (`composables/useCatalogo.ts`) |
| Organización por categorías | Inicio → categoría (`/categoria/ramos`) → detalle (`/articulo/<id>`) |
| Búsqueda | Campo en la cabecera → `/buscar?q=rosas` (ignora tildes y mayúsculas) |
| Paginación | 6 artículos por página, en categorías y en resultados de búsqueda |
| Snipcart | Botón «Agregar al carrito» en cada artículo y opción «Carrito» en el menú principal |
| Utterances | Comentarios en la página de cada artículo |
| Hosting | Netlify (`netlify.toml` incluido) |

## Estructura

```
data/            catálogo en JSON (artículos y categorías)
public/img/      38 imágenes SVG propias, una por artículo
components/      cabecera, buscador, tarjeta, botón de compra, paginación, comentarios
composables/     useCatalogo.ts (consultas, búsqueda y paginación)
pages/           index, categoria/[slug]/[[pagina]], articulo/[id], buscar
scripts/         generar_catalogo.py (regenera JSON e imágenes)
```

## 1. Probar localmente

Requiere **Node.js 18.20 o superior** (recomendado 20).

```bash
npm install
cp .env.example .env      # en Windows: copy .env.example .env
npm run dev
```

Abra http://localhost:3000. Sin configurar nada ya funcionan categorías, búsqueda y paginación. Para el carrito y los comentarios complete el `.env` (siguientes pasos), reinicie `npm run dev` y recargue.

### Snipcart (carrito)

1. Cree una cuenta gratuita en https://app.snipcart.com.
2. En **Account → API keys** copie la clave **pública de TEST** y péguela en `NUXT_PUBLIC_SNIPCART_KEY`.
3. En **Account → Store settings → Domains & URLs** registre el dominio (para pruebas locales `localhost:3000`; luego el de Netlify) y deje habilitado el modo de pruebas.
4. Los precios están en **USD**; es la moneda por defecto de Snipcart. Puede cambiarla en el panel si lo desea.
5. Pruebe: «Agregar al carrito» → se abre el carrito lateral; el contador del menú se actualiza.

Nota: Snipcart valida precios leyendo la URL de cada producto (`data-item-url`). Esa validación solo funciona en el sitio publicado, por lo que en modo TEST local puede mostrar avisos de validación; después de publicar debe funcionar con normalidad.

### Utterances (comentarios)

1. Cree un repositorio **público** en GitHub (por ejemplo `floreria-comentarios`).
2. Instale la app https://github.com/apps/utterances en ese repositorio.
3. Ponga `NUXT_PUBLIC_UTTERANCES_REPO=su-usuario/floreria-comentarios` en `.env`.
4. Abra cualquier artículo, inicie sesión con GitHub y deje un comentario; aparecerá como Issue en el repositorio.

## 2. Publicar en Netlify

**Opción A — con Git (recomendada):**
1. Suba el proyecto a un repositorio de GitHub (`.gitignore` ya excluye `node_modules`, `.nuxt` y `.output`).
2. En Netlify: **Add new site → Import an existing project** y elija el repositorio. Netlify toma el comando y la carpeta de `netlify.toml` (`npm run generate`, `.output/public`).
3. En **Site configuration → Environment variables** agregue `NUXT_PUBLIC_SNIPCART_KEY` y `NUXT_PUBLIC_UTTERANCES_REPO`.
4. Haga **Deploy**. Después registre el dominio `https://su-sitio.netlify.app` en Snipcart (paso 3 de arriba).

**Opción B — carga manual:**
```bash
npm run generate
```
Arrastre la carpeta `.output/public` a https://app.netlify.com/drop (defina las claves en el `.env` antes de generar, ya que se incluyen en el sitio).

## 3. Entregables para el Aula Virtual

1. **Código fuente** en un `.zip` **sin** `node_modules`, `.nuxt`, `.output` ni `dist` (el sitio generado no se debe subir). El zip de este proyecto ya viene limpio.
2. **URL del sitio publicado** (Netlify).
3. Este `README.md` con instrucciones.

## 4. Datos del estudiante

Nombre: Isaac Felipe Brenes Calderón Cédula: 1-1904-0860  Tema: 7. Tienda de flores (Floristería)

## Regenerar el catálogo (opcional)

`npm run catalogo` (requiere Python 3) vuelve a crear `data/*.json` y las imágenes SVG.
