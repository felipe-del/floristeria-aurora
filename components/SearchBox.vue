<script setup lang="ts">
const route = useRoute()
const texto = ref('')

// Mantiene el texto buscado cuando se está en la página de resultados
watch(() => route.query.q, q => { texto.value = typeof q === 'string' ? q : '' }, { immediate: true })

function buscar() {
  const q = texto.value.trim()
  if (q) navigateTo({ path: '/buscar', query: { q } })
}
</script>

<template>
  <form class="buscador" role="search" @submit.prevent="buscar">
    <label for="q" class="sr-only">Buscar en la tienda</label>
    <input id="q" v-model="texto" type="search" placeholder="Buscar rosas, orquídeas, boda…" autocomplete="off">
    <button type="submit" class="btn btn--oscuro">Buscar</button>
  </form>
</template>
