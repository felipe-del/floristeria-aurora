<script setup lang="ts">
import type { Articulo } from '~/composables/useCatalogo'
defineProps<{ articulo: Articulo }>()
const { nombreCategoria } = useCatalogo()
</script>

<template>
  <article class="tarjeta">
    <NuxtLink :to="`/articulo/${articulo.id}`" class="tarjeta__imagen" :aria-label="`Ver detalle de ${articulo.nombre}`">
      <img :src="articulo.imagen" :alt="articulo.nombre" width="600" height="600" loading="lazy">
    </NuxtLink>
    <div class="tarjeta__cuerpo">
      <p class="tarjeta__cat">{{ nombreCategoria(articulo.categoria) }}</p>
      <h3><NuxtLink :to="`/articulo/${articulo.id}`">{{ articulo.nombre }}</NuxtLink></h3>
      <p class="tarjeta__precio">{{ formatoPrecio(articulo.precio) }}</p>
      <BuyButton :articulo="articulo" />
    </div>
  </article>
</template>
