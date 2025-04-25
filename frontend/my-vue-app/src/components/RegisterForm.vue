<template>
    <div class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-form">
        <h2>Register</h2>
        <form @submit.prevent="handleRegister">
          <div v-if="error" class="error-message">{{ error }}</div>
          <input type="text" v-model="name" placeholder="Name" required />
          <input type="email" v-model="email" placeholder="Email" required />
          <input type="password" v-model="password" placeholder="Password" required />
          <button class="auth-btn" type="submit">Register</button>
        </form>
        <p>
          Already have an account?
          <span class="modal-link" @click="$emit('switch-to-login')">Login</span>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  // import axios from 'axios';
  import api from '@/api';
  
  export default {
    name: "RegisterForm",
    data() {
      return {
        name: "",
        email: "",
        password: "",
        error: null
      };
    },
    methods: {
      async handleRegister() {
        try {
          // Send POST request to Flask backend
          const response = await api.post('/api/register', {
            // Only email and password are used by your backend, but you can send name if you add support
            name:this.name,
            email: this.email,
            password: this.password
          });
          // Success: emit event or show a message
          this.$emit('register-success', response.data);
          this.$emit('close');
          this.error = null;
        } catch (err) {
          if (err.response && err.response.data && err.response.data.error) {
            this.error = err.response.data.error;
          } else {
            this.error = "An error occurred. Please try again.";
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(12,27,58,0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
  }
  .modal-form {
    background: rgba(255,255,255,0.95);
    border-radius: 18px;
    padding: 32px 28px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    min-width: 320px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .modal-form h2 {
    margin-bottom: 8px;
    color: #0c1b3a;
  }
  .modal-form input {
    border: 1px solid #ddd;
    border-radius: 25px;
    padding: 10px 18px;
    font-size: 1rem;
    margin-bottom: 10px;
    outline: none;
  }
  .modal-form input:focus {
    border-color: #4da6ff;
    box-shadow: 0 0 0 2px rgba(77,166,255,0.15);
  }
  .auth-btn {
    background: #4da6ff;
    color: #fff;
    border: none;
    border-radius: 30px;
    padding: 8px 22px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s;
    box-shadow: 0 4px 15px rgba(77,166,255,0.2);
  }
  .auth-btn:hover {
    background: #1a85ff;
  }
  .modal-link {
    color: #4da6ff;
    cursor: pointer;
    font-weight: 500;
    text-decoration: underline;
  }
  .error-message {
    color: #e74c3c;
    margin-bottom: 10px;
    font-size: 0.98rem;
  }
  </style>
  