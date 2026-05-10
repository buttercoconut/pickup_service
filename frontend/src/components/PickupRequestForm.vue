<template>
  <div class="pickup-form">
    <h2>Request a Pickup</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name</label>
        <input v-model="form.name" id="name" type="text" required />
      </div>
      <div class="form-group">
        <label for="address">Address</label>
        <input v-model="form.address" id="address" type="text" required />
      </div>
      <div class="form-group">
        <label for="date">Pickup Date</label>
        <input v-model="form.date" id="date" type="date" required />
      </div>
      <div class="form-group">
        <label for="time">Pickup Time</label>
        <input v-model="form.time" id="time" type="time" required />
      </div>
      <div class="form-group">
        <label for="items">Items</label>
        <textarea v-model="form.items" id="items" rows="3" required></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import axios from 'axios'

const form = reactive({
  name: '',
  address: '',
  date: '',
  time: '',
  items: ''
})

const submitForm = async () => {
  try {
    const response = await axios.post('/api/pickup', form)
    alert('Pickup requested successfully! Reference ID: ' + response.data.id)
    Object.assign(form, { name: '', address: '', date: '', time: '', items: '' })
  } catch (error) {
    console.error(error)
    alert('Failed to request pickup. Please try again.')
  }
}
</script>

<style scoped>
.pickup-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input, textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}
button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #369870;
}
</style>
