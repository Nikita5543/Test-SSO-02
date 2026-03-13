<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const userStore = useUserStore()

// Получаем пункты меню из плагинов (заглушка — можно хранить в store)
const menuItems = [
  { title: 'Dashboard', icon: 'HomeIcon', path: '/' },
  { title: 'Пользователи', icon: 'UserGroupIcon', path: '/users' },
  { title: 'Настройки', icon: 'CogIcon', path: '/settings' }
]

// Пример: добавим пункт от плагина (в реальности — из pluginManager)
menuItems.push({ title: 'Мониторинг', icon: 'ChartBarIcon', path: '/monitoring' })

const isActive = (path) => route.path === path
</script>

<template>
  <aside class="w-64 bg-white dark:bg-gray-800 shadow-lg fixed inset-y-0 left-0 transform transition-transform duration-300 z-50">
    <div class="p-6">
      <h1 class="text-xl font-bold text-indigo-600 dark:text-indigo-400">NetOps</h1>
    </div>
    <nav class="mt-6 px-4">
      <router-link
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        class="flex items-center px-4 py-3 rounded-lg mb-2 transition-colors"
        :class="{ 'bg-indigo-100 dark:bg-indigo-900': isActive(item.path) }"
      >
        <component :is="item.icon" class="w-5 h-5 mr-3" />
        {{ item.title }}
      </router-link>
    </nav>
  </aside>
</template>