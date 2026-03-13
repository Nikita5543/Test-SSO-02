javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import './assets/tailwind.css'

const pinia = createPinia()
const app = createApp(App)

// Реестр плагинов
const pluginManager = {
  routes: [],
  menuItems: [],
  addRoute(route) { this.routes.push(route) },
  addMenu(item) { this.menuItems.push(item) }
}

// Динамическая загрузка плагинов
async function loadPlugins() {
  const pluginModules = import.meta.glob('./plugins/*/index.js', { eager: false })
  for (const path of Object.keys(pluginModules)) {
    const module = await pluginModules[path]()
    if (module.register) {
      module.register(pluginManager)
    }
  }
  // Добавляем маршруты плагинов
  pluginManager.routes.forEach(route => router.addRoute(route))
}

loadPlugins().then(() => {
  app.use(pinia).use(router).mount('#app')
})