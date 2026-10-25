<script setup lang="ts">
import type { Articulo } from '~/composables/useCatalogo'
defineProps<{ items: Articulo[] }>()
</script>

<template>
  <ul class="rejilla">
    <li v-for="a in items" :key="a.id"><ProductCard :articulo="a" /></li>
  </ul>
</template>
