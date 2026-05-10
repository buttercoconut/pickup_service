import { createRouter, createWebHistory } from 'vue-router';
import PickupRequestForm from '@/components/PickupRequestForm.vue';
import CustomerDashboard from '@/views/CustomerDashboard.vue';

const routes = [
  { path: '/', component: PickupRequestForm },
  { path: '/dashboard', component: CustomerDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;