<script setup lang="ts">
const { getCategorias } = useCatalogo()
const categorias = getCategorias()
</script>

<template>
  <header class="cabecera">
    <div class="contenedor cabecera__fila">
      <NuxtLink to="/" class="marca" aria-label="Floristería Aurora, ir al inicio">
        <img src="/favicon.svg" alt="" width="34" height="34">
        <span>Floristería Aurora</span>
      </NuxtLink>
      <SearchBox class="cabecera__buscar" />
      <button class="carrito snipcart-checkout" type="button" aria-label="Abrir carrito de compras">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M3 4h2l2.4 11h10.2L20 7H6.2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9" cy="19" r="1.5" fill="currentColor"/><circle cx="17" cy="19" r="1.5" fill="currentColor"/></svg>
        <span>Carrito</span>
        <span class="carrito__cuenta snipcart-items-count">0</span>
      </button>
    </div>
    <nav class="contenedor menu" aria-label="Categorías">
      <NuxtLink to="/" exact-active-class="activo">Inicio</NuxtLink>
      <NuxtLink v-for="c in categorias" :key="c.slug" :to="`/categoria/${c.slug}`" active-class="activo">{{ c.nombre }}</NuxtLink>
    </nav>
  </header>
</template>
