<script setup lang="ts">
const route = useRoute()
const { getArticulo, getCategoria, nombreCategoria, relacionados } = useCatalogo()

const articulo = getArticulo(route.params.id as string)
if (!articulo) throw createError({ statusCode: 404, statusMessage: 'Artículo no encontrado', fatal: true })

const categoria = getCategoria(articulo.categoria)!
const otros = relacionados(articulo)

const ficha = [
  ['Categoría', nombreCategoria(articulo.categoria)],
  ['Contenido', articulo.contenido],
  ['Tamaño', articulo.tamano],
  ['Color', articulo.color],
  ['Ocasión', articulo.ocasion]
]

useSeoMeta({
  title: `${articulo.nombre} · Floristería Aurora`,
  description: articulo.descripcion,
  ogTitle: articulo.nombre,
  ogDescription: articulo.descripcion,
  ogImage: articulo.imagen
})
</script>

<template>
  <div class="contenedor seccion">
    <nav class="migas" aria-label="Ruta de navegación">
      <NuxtLink to="/">Inicio</NuxtLink> /
      <NuxtLink :to="`/categoria/${categoria.slug}`">{{ categoria.nombre }}</NuxtLink> /
      <span>{{ articulo!.nombre }}</span>
    </nav>

    <article class="detalle">
      <img class="detalle__imagen" :src="articulo!.imagen" :alt="articulo!.nombre" width="600" height="600">
      <div class="detalle__info">
        <h1>{{ articulo!.nombre }}</h1>
        <p class="detalle__precio">{{ formatoPrecio(articulo!.precio) }}</p>
        <p>{{ articulo!.descripcion }}</p>
        <dl class="ficha">
          <template v-for="[k, v] in ficha" :key="k">
            <dt>{{ k }}</dt><dd>{{ v }}</dd>
          </template>
        </dl>
        <BuyButton :articulo="articulo!" grande />
        <p class="nota-cuidados">{{ categoria.cuidados }}</p>
      </div>
    </article>

    <UtterancesComments />

    <section v-if="otros.length" class="seccion" aria-labelledby="h-rel">
      <h2 id="h-rel">Más en {{ categoria.nombre }}</h2>
      <ProductGrid :items="otros" />
    </section>
  </div>
</template>
