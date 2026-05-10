<template>
  <router-view />
</template>

<script setup>
import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import CustomerDashboard from './views/CustomerDashboard.vue'

const routes = [
  { path: '/', component: CustomerDashboard }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App).use(router).mount('#app')
</script>
