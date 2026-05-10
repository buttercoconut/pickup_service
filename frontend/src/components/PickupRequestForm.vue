<template>
  <div class="pickup-request-form">
    <h2>픽업 요청</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="customerName">이름</label>
        <input type="text" id="customerName" v-model="form.customerName" required />
      </div>
      <div class="form-group">
        <label for="contact">연락처</label>
        <input type="tel" id="contact" v-model="form.contact" required />
      </div>
      <div class="form-group">
        <label for="address">주소</label>
        <input type="text" id="address" v-model="form.address" required />
      </div>
      <div class="form-group">
        <label for="pickupTime">픽업 예정 시간</label>
        <input type="datetime-local" id="pickupTime" v-model="form.pickupTime" required />
      </div>
      <div class="form-group">
        <label for="itemDescription">물품 설명</label>
        <textarea id="itemDescription" v-model="form.itemDescription" required></textarea>
      </div>
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import axios from 'axios';

const form = reactive({
  customerName: '',
  contact: '',
  address: '',
  pickupTime: '',
  itemDescription: '',
});

const submitForm = async () => {
  try {
    const payload = {
      customer_name: form.customerName,
      contact: form.contact,
      address: form.address,
      pickup_time: form.pickupTime,
      item_description: form.itemDescription,
    };
    const response = await axios.post('/api/pickup-requests', payload);
    alert('픽업 요청이 접수되었습니다! ID: ' + response.data.id);
    // reset form
    form.customerName = '';
    form.contact = '';
    form.address = '';
    form.pickupTime = '';
    form.itemDescription = '';
  } catch (error) {
    console.error(error);
    alert('픽업 요청 제출 중 오류가 발생했습니다.');
  }
};
</script>

<style scoped>
.pickup-request-form {
  max-width: 600px;
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
