<script setup lang="ts">
import type { Articulo } from '~/composables/useCatalogo'
defineProps<{ articulo: Articulo; grande?: boolean }>()
</script>

<template>
  <!-- Botón de compra de Snipcart: los atributos data-item-* describen el producto -->
  <button
    type="button"
    class="btn snipcart-add-item"
    :class="{ 'btn--grande': grande }"
    :data-item-id="articulo.id"
    :data-item-name="articulo.nombre"
    :data-item-price="articulo.precio"
    :data-item-url="`/articulo/${articulo.id}`"
    :data-item-description="articulo.descripcion"
    :data-item-image="articulo.imagen"
    data-item-quantity="1"
  >
    Agregar al carrito
  </button>
</template>
