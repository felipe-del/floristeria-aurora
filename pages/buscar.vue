<script setup lang="ts">
const route = useRoute()
const { buscar, paginar } = useCatalogo()

const q = computed(() => (typeof route.query.q === 'string' ? route.query.q : ''))
const numero = computed(() => parseInt(String(route.query.pagina || '1'), 10))
const resultados = computed(() => buscar(q.value))
const pag = computed(() => paginar(resultados.value, numero.value))
const enlace = (n: number) => ({ path: '/buscar', query: { q: q.value, ...(n > 1 ? { pagina: n } : {}) } })

useSeoMeta({ title: 'Buscar · Floristería Aurora', robots: 'noindex' })
</script>

<template>
  <div class="contenedor seccion">
    <h1>Resultados de búsqueda</h1>
    <!-- Los resultados dependen de la URL, por eso se muestran solo en el navegador -->
    <ClientOnly>
      <p v-if="!q" class="intro">Escribí una palabra clave arriba, por ejemplo “rosas”, “orquídea” o “boda”.</p>
      <template v-else>
        <p class="resumen">
          {{ pag.cantidad }} {{ pag.cantidad === 1 ? 'resultado' : 'resultados' }} para “{{ q }}”
          <template v-if="pag.total > 1"> · página {{ pag.actual }} de {{ pag.total }}</template>
        </p>
        <ProductGrid v-if="pag.cantidad" :items="pag.items" />
        <div v-else class="vacio">
          <p>No encontramos artículos con esas palabras. Probá con otro término o explorá las categorías.</p>
          <NuxtLink to="/" class="btn">Ver categorías</NuxtLink>
        </div>
        <PaginationNav :actual="pag.actual" :total="pag.total" :enlace="enlace" />
      </template>
    </ClientOnly>
  </div>
</template>
