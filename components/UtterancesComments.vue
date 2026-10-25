<script setup lang="ts">
// Comentarios con Utterances (los comentarios se guardan como Issues de GitHub).
const { utterancesRepo } = useRuntimeConfig().public
const route = useRoute()
const contenedor = ref<HTMLElement | null>(null)

function cargar() {
  if (!contenedor.value || !utterancesRepo) return
  contenedor.value.innerHTML = ''
  const s = document.createElement('script')
  s.src = 'https://utteranc.es/client.js'
  s.async = true
  s.crossOrigin = 'anonymous'
  s.setAttribute('repo', utterancesRepo)
  s.setAttribute('issue-term', 'pathname')
  s.setAttribute('theme', 'github-light')
  contenedor.value.appendChild(s)
}

onMounted(cargar)
watch(() => route.path, () => nextTick(cargar))
</script>

<template>
  <section class="comentarios" aria-labelledby="titulo-comentarios">
    <h2 id="titulo-comentarios">Comentarios</h2>
    <p v-if="!utterancesRepo" class="aviso">
      Falta configurar <code>NUXT_PUBLIC_UTTERANCES_REPO</code> (ver README).
    </p>
    <!-- Contenedor vacío: el script se inserta solo en el navegador -->
    <div ref="contenedor" />
  </section>
</template>
