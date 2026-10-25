<script setup lang="ts">
const { snipcartKey } = useRuntimeConfig().public

onMounted(() => {
  // Carrito de Snipcart en español
  document.addEventListener('snipcart.initialized', () => {
    ;(window as any).Snipcart?.api?.session?.setLanguage('es')
  })
})
</script>

<template>
  <div>
    <a class="saltar" href="#contenido">Saltar al contenido</a>
    <SiteHeader />
    <main id="contenido">
      <NuxtPage />
    </main>
    <SiteFooter />
    <!-- Contenedor requerido por Snipcart -->
    <div id="snipcart" hidden :data-api-key="snipcartKey" data-config-modal-style="side" data-config-add-product-behavior="overlay" />
  </div>
</template>
