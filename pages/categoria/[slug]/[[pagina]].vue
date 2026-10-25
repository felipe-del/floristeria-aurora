<script setup lang="ts">
const route = useRoute()
const { getCategoria, articulosDeCategoria, paginar } = useCatalogo()

const slug = route.params.slug as string
const categoria = getCategoria(slug)
if (!categoria) throw createError({ statusCode: 404, statusMessage: 'Categoría no encontrada', fatal: true })

const numero = parseInt((route.params.pagina as string) || '1', 10)
const lista = articulosDeCategoria(slug)
const pag = paginar(lista, numero)
if (numero !== pag.actual && route.params.pagina) {
  throw createError({ statusCode: 404, statusMessage: 'Página no encontrada', fatal: true })
}

const enlace = (n: number) => (n === 1 ? `/categoria/${slug}` : `/categoria/${slug}/${n}`)

useSeoMeta({
  title: `${categoria.nombre} · Floristería Aurora`,
  description: categoria.descripcion
})
</script>

<template>
  <div class="contenedor seccion">
    <nav class="migas" aria-label="Ruta de navegación">
      <NuxtLink to="/">Inicio</NuxtLink> / <span>{{ categoria!.nombre }}</span>
    </nav>
    <h1>{{ categoria!.nombre }}</h1>
    <p class="intro">{{ categoria!.descripcion }}</p>
    <p class="resumen">{{ pag.cantidad }} artículos · página {{ pag.actual }} de {{ pag.total }}</p>

    <ProductGrid :items="pag.items" />
    <PaginationNav :actual="pag.actual" :total="pag.total" :enlace="enlace" />
    <p class="nota-cuidados">{{ categoria!.cuidados }}</p>
  </div>
</template>
