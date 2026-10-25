<script setup lang="ts">
defineProps<{ error: { statusCode?: number; message?: string } }>()
const volver = () => clearError({ redirect: '/' })
</script>

<template>
  <div>
    <SiteHeader />
    <main id="contenido" class="contenedor vacio">
      <h1>Esta página no existe</h1>
      <p>El enlace que abriste no corresponde a ningún producto ni categoría de la tienda.</p>
      <button class="btn" @click="volver">Volver al inicio</button>
    </main>
    <SiteFooter />
  </div>
</template>
