<template>
  <div class="dashboard">
    <h2>Welcome, {{ userName }}</h2>
    <PickupRequestForm @submitted="onPickupSubmitted" />
    <div class="pickup-history">
      <h3>Your Pickup History</h3>
      <ul>
        <li v-for="(pickup, index) in pickups" :key="index">
          {{ pickup.date }} {{ pickup.time }} - {{ pickup.items }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import PickupRequestForm from '../components/PickupRequestForm.vue'

const userName = ref('Customer')
const pickups = ref([])

const fetchHistory = async () => {
  try {
    const res = await axios.get('/api/pickup/history')
    pickups.value = res.data
  } catch (err) {
    console.error(err)
  }
}

const onPickupSubmitted = () => {
  fetchHistory()
}

onMounted(() => {
  fetchHistory()
})
</script>

<style scoped>
dashboard {
  padding: 1rem;
}
.pickup-history {
  margin-top: 2rem;
}
</style>
