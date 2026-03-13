<script setup>
import { ref } from 'vue'
import Sidebar from './components/layout/Sidebar.vue'
import Header from './components/layout/Header.vue'

const sidebarOpen = ref(false)
</script>

<template>
  <div class="flex h-screen bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200">
    <Sidebar :open="sidebarOpen" @close="sidebarOpen = false" />
    <div class="flex flex-col flex-1 overflow-hidden">
      <Header @toggle-sidebar="sidebarOpen = !sidebarOpen" />
      <main class="flex-1 overflow-y-auto p-6">
        <router-view />
      </main>
    </div>
  </div>
</template>