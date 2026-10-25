<script setup lang="ts">
// "enlace" recibe el número de página y devuelve la ruta (string u objeto de ruta)
const props = defineProps<{ actual: number; total: number; enlace: (n: number) => any }>()
const paginas = computed(() => Array.from({ length: props.total }, (_, i) => i + 1))
</script>

<template>
  <nav v-if="total > 1" class="paginacion" aria-label="Paginación">
    <NuxtLink v-if="actual > 1" :to="enlace(actual - 1)" rel="prev" class="paginacion__nav">← Anterior</NuxtLink>
    <span v-else class="paginacion__nav paginacion__nav--off" aria-disabled="true">← Anterior</span>

    <NuxtLink
      v-for="n in paginas" :key="n" :to="enlace(n)"
      class="paginacion__num" :class="{ 'paginacion__num--actual': n === actual }"
      :aria-current="n === actual ? 'page' : undefined"
    >{{ n }}</NuxtLink>

    <NuxtLink v-if="actual < total" :to="enlace(actual + 1)" rel="next" class="paginacion__nav">Siguiente →</NuxtLink>
    <span v-else class="paginacion__nav paginacion__nav--off" aria-disabled="true">Siguiente →</span>
  </nav>
</template>
