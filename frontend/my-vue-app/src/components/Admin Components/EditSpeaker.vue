<template>
  <div class="admin-edit-speaker-page">
    <AdminNavbar />
    <div class="admin-form-container">
      <h2>Edit Speaker</h2>
      <form @submit.prevent="updateSpeaker">
        <div class="form-group">
          <label>Model Name:</label>
          <input v-model="speaker.model_name" required />
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Magnet Size:</label>
            <input v-model="speaker.magnet_size" />
          </div>
          <div class="form-group">
            <label>Power Rating:</label>
            <input v-model="speaker.power_rating" />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Voice Coil Diameter:</label>
            <input v-model="speaker.voice_coil_diameter" />
          </div>
          <div class="form-group">
            <label>Voice Coil Type:</label>
            <input v-model="speaker.voice_coil_type" />
          </div>
        </div>
        <div class="form-group">
          <label>Update Image:</label>
          <input type="file" @change="handleFileUpload" />
          <div v-if="speaker.image_url">
            <img :src="speaker.image_url" alt="Current Image" class="speaker-img-preview" />
          </div>
        </div>
        <button type="submit" class="submit-btn">Update Speaker</button>
      </form>
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";
import api from '@/api';

export default {
  name: "EditSpeaker",
  components: { AdminNavbar },
  data() {
    return {
      speaker: {
        model_name: '',
        magnet_size: '',
        power_rating: '',
        voice_coil_diameter: '',
        voice_coil_type: '',
        image: null,
        image_url: ''
      }
    };
  },
  mounted() {
    this.fetchSpeaker();
  },
  methods: {
    async fetchSpeaker() {
      try {
        const res = await api.get(`/api/speakers/${this.$route.params.id}`);
        this.speaker = res.data;
      } catch (err) {
        alert('Failed to load speaker');
      }
    },
    handleFileUpload(event) {
      this.speaker.image = event.target.files[0];
    },
    async updateSpeaker() {
      try {
        const formData = new FormData();
        formData.append('model_name', this.speaker.model_name);
        formData.append('magnet_size', this.speaker.magnet_size);
        formData.append('power_rating', this.speaker.power_rating);
        formData.append('voice_coil_diameter', this.speaker.voice_coil_diameter);
        formData.append('voice_coil_type', this.speaker.voice_coil_type);
        if (this.speaker.image) {
          formData.append('image', this.speaker.image);
        }
        await api.put(`/api/speakers/${this.$route.params.id}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        this.$router.push('/admin/speakers');
      } catch (err) {
        alert('Failed to update speaker');
      }
    }
  }
};
</script>

<style scoped>
.admin-edit-speaker-page {
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

.speaker-img-preview {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 8px;
  margin-top: 8px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.10);
  border: 1px solid #e0e0e0;
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
