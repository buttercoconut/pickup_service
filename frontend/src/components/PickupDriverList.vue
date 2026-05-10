<template>
  <div>
    <h2>Pickup Driver List</h2>
    <ul>
      <li v-for="driver in drivers" :key="driver.id">
        {{ driver.name }} - {{ driver.vehicle }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const drivers = ref([]);

onMounted(async () => {
  try {
    const res = await axios.get('/api/pickup_drivers');
    drivers.value = res.data;
  } catch (e) {
    console.error(e);
  }
});
</script>

<style scoped>
/* Add styles as needed */
</style>