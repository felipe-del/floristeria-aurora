import { readFileSync } from 'node:fs'

// Cantidad de artículos por página (única fuente de verdad)
const POR_PAGINA = 6

const articulos = JSON.parse(readFileSync('./data/articulos.json', 'utf-8'))
const categorias = JSON.parse(readFileSync('./data/categorias.json', 'utf-8'))

// Rutas a pre-renderizar para el sitio estático (npm run generate)
const rutas: string[] = ['/', '/buscar']
for (const c of categorias) {
  const total = articulos.filter((a: any) => a.categoria === c.slug).length
  const paginas = Math.max(1, Math.ceil(total / POR_PAGINA))
  rutas.push(`/categoria/${c.slug}`)
  for (let p = 2; p <= paginas; p++) rutas.push(`/categoria/${c.slug}/${p}`)
}
for (const a of articulos) rutas.push(`/articulo/${a.id}`)

const SNIPCART_VERSION = '3.7.1'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      porPagina: POR_PAGINA,
      // Se definen con variables de entorno (ver .env.example)
      snipcartKey: '',     // NUXT_PUBLIC_SNIPCART_KEY
      utterancesRepo: ''   // NUXT_PUBLIC_UTTERANCES_REPO  (usuario/repositorio)
    }
  },

  nitro: {
    prerender: { routes: rutas, crawlLinks: true, failOnError: false }
  },

  app: {
    head: {
      htmlAttrs: { lang: 'es' },
      title: 'Floristería Aurora',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Floristería Aurora: ramos, arreglos, plantas y orquídeas con compra en línea.' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap' },
        { rel: 'preconnect', href: 'https://app.snipcart.com' },
        { rel: 'preconnect', href: 'https://cdn.snipcart.com' },
        { rel: 'stylesheet', href: `https://cdn.snipcart.com/themes/v${SNIPCART_VERSION}/default/snipcart.css` }
      ],
      script: [
        { src: `https://cdn.snipcart.com/themes/v${SNIPCART_VERSION}/default/snipcart.js`, defer: true }
      ]
    }
  }
})
