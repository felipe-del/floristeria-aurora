<script setup lang="ts">
const { getCategorias, contarCategoria, destacados } = useCatalogo()
const categorias = getCategorias()
const lista = destacados()

useSeoMeta({
  title: 'Floristería Aurora · Flores y plantas con envío',
  description: 'Ramos, arreglos florales, plantas de interior, orquídeas y flores para bodas. Compra en línea.'
})
</script>

<template>
  <div>
    <section class="hero">
      <div class="contenedor hero__fila">
        <div class="hero__texto">
          <h1>Flores que llegan frescas, armadas el mismo día.</h1>
          <p>Elegí un ramo, un arreglo o una planta, agregalo al carrito y pagá en línea.</p>
          <NuxtLink class="btn btn--grande" to="/categoria/ramos">Ver ramos</NuxtLink>
        </div>
        <img class="hero__imagen" src="/img/ramo-de-peonias-rosadas.svg" alt="Ramo de peonías rosadas" width="600" height="600">
      </div>
    </section>

    <section class="contenedor seccion" aria-labelledby="h-categorias">
      <h2 id="h-categorias">Comprar por categoría</h2>
      <ul class="categorias">
        <li v-for="c in categorias" :key="c.slug">
          <NuxtLink :to="`/categoria/${c.slug}`" class="categoria">
            <img :src="c.imagen" alt="" width="600" height="600" loading="lazy">
            <span class="categoria__nombre">{{ c.nombre }}</span>
            <span class="categoria__cuenta">{{ contarCategoria(c.slug) }} artículos</span>
          </NuxtLink>
        </li>
      </ul>
    </section>

    <section class="contenedor seccion" aria-labelledby="h-destacados">
      <h2 id="h-destacados">Más pedidos esta semana</h2>
      <ProductGrid :items="lista" />
    </section>
  </div>
</template>
