<template>
  <div class="admin-add-speaker-page">
    <AdminNavbar />
    <div class="admin-form-container">
      <h2>Add New Speaker</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label>Model Name:</label>
          <input v-model="speaker.model_name" required>
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label>Magnet Size:</label>
            <input v-model="speaker.magnet_size">
          </div>
          <div class="form-group">
            <label>Power Rating:</label>
            <input v-model="speaker.power_rating">
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Voice Coil Diameter:</label>
            <input v-model="speaker.voice_coil_diameter">
          </div>
          <div class="form-group">
            <label>Voice Coil Type:</label>
            <input v-model="speaker.voice_coil_type">
          </div>
        </div>

        <div class="form-group">
          <label>Upload Image:</label>
          <input type="file" @change="handleFileUpload">
        </div>

        <button type="submit" class="submit-btn">Save Speaker</button>
      </form>
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";
import api from '@/api';

export default {
  components: { AdminNavbar },
  data() {
    return {
      speaker: {
        model_name: '',
        magnet_size: '',
        power_rating: '',
        voice_coil_diameter: '',
        voice_coil_type: '',
        image: null
      }
    };
  },
  methods: {
    handleFileUpload(event) {
      this.speaker.image = event.target.files[0];
    },
    async submitForm() {
      const formData = new FormData();
      Object.entries(this.speaker).forEach(([key, value]) => {
        if (value) formData.append(key, value);
      });

      try {
        await api.post('/api/speakers', formData, {
          headers: {'Content-Type': 'multipart/form-data'}
        });
        this.$router.push('/admin/speakers');
      } catch (error) {
        console.error('Error saving speaker:', error);
      }
    }
  }
};
</script>

<style scoped>
.admin-add-speaker-page {
  min-height: 100vh;
  background: #f5f7fa;
}

.admin-form-container {
  max-width: 500px;
  margin: 40px auto;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 6px 32px rgba(0,0,0,0.12);
  padding: 32px 28px 24px 28px;
}

h2 {
  margin-bottom: 24px;
  color: #1976d2;
  font-weight: 700;
  letter-spacing: 1px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-row {
  display: flex;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  flex: 1;
}

label {
  margin-bottom: 7px;
  color: #2c3e50;
  font-size: 15px;
  font-weight: 600;
}

input[type="text"],
input[type="file"],
input:not([type="file"]) {
  padding: 8px 10px;
  border: 1px solid #d0d0d0;
  border-radius: 6px;
  font-size: 15px;
  background: #f8fafd;
  transition: border 0.2s;
}

input:focus {
  border-color: #1976d2;
  outline: none;
}

.submit-btn {
  background: #1976d2;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 11px 0;
  font-size: 17px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 18px;
  transition: background 0.2s;
}
.submit-btn:hover {
  background: #125ea2;
}

@media (max-width: 600px) {
  .admin-form-container {
    padding: 15px 4px;
  }
  .form-row {
    flex-direction: column;
    gap: 0;
  }
}
</style>
