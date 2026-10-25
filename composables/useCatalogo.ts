import articulos from '~/data/articulos.json'
import categorias from '~/data/categorias.json'

export type Articulo = (typeof articulos)[number]
export type Categoria = (typeof categorias)[number]

/** Quita tildes y pasa a minúsculas para comparar texto. */
export const normalizar = (s: string) =>
  s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim()

export const formatoPrecio = (n: number) =>
  new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(n)

export function useCatalogo() {
  const porPagina = Number(useRuntimeConfig().public.porPagina) || 6

  const getCategorias = () => categorias
  const getCategoria = (slug: string) => categorias.find(c => c.slug === slug)
  const getArticulo = (id: string) => articulos.find(a => a.id === id)
  const nombreCategoria = (slug: string) => getCategoria(slug)?.nombre ?? slug
  const articulosDeCategoria = (slug: string) => articulos.filter(a => a.categoria === slug)
  const destacados = () => articulos.filter(a => a.destacado)
  const relacionados = (a: Articulo, n = 3) =>
    articulos.filter(x => x.categoria === a.categoria && x.id !== a.id).slice(0, n)
  const contarCategoria = (slug: string) => articulosDeCategoria(slug).length

  /** Búsqueda por palabras clave (todas deben aparecer) en los campos del artículo. */
  const buscar = (texto: string) => {
    const palabras = normalizar(texto).split(/\s+/).filter(Boolean)
    if (!palabras.length) return []
    return articulos.filter(a => {
      const pajar = normalizar([
        a.nombre, a.descripcion, nombreCategoria(a.categoria), a.color,
        a.ocasion, a.contenido, a.tamano, a.etiquetas.join(' ')
      ].join(' '))
      return palabras.every(p => pajar.includes(p))
    })
  }

  const paginar = <T>(lista: T[], pagina: number) => {
    const total = Math.max(1, Math.ceil(lista.length / porPagina))
    const actual = Math.min(Math.max(1, pagina || 1), total)
    return { items: lista.slice((actual - 1) * porPagina, actual * porPagina), actual, total, cantidad: lista.length }
  }

  return { getCategorias, getCategoria, getArticulo, nombreCategoria, articulosDeCategoria, destacados, relacionados, contarCategoria, buscar, paginar }
}
