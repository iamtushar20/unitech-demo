<template>
  <div class="admin-speaker-list-page">
    <AdminNavbar />
    <div class="admin-form-container">
      <h2>Speakers List</h2>
      <router-link to="/admin/add-speaker">
        <button class="submit-btn">Add Speaker</button>
      </router-link>
      <table class="admin-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Model Name</th>
            <th>Magnet Size</th>
            <th>Power Rating</th>
            <th>Voice Coil Diameter</th>
            <th>Voice Coil Type</th>
            <th>Image</th>
            <th>Date Added</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="speaker in speakers" :key="speaker.id">
            <td>{{ speaker.id }}</td>
            <td>{{ speaker.model_name }}</td>
            <td>{{ speaker.magnet_size }}</td>
            <td>{{ speaker.power_rating }}</td>
            <td>{{ speaker.voice_coil_diameter }}</td>
            <td>{{ speaker.voice_coil_type }}</td>
            <td>
              <img v-if="speaker.image_url" :src="speaker.image_url" alt="Speaker Image" class="speaker-img">
            </td>
            <td>{{ formatDate(speaker.date_added) }}</td>
            <td>
              <router-link :to="`/admin/edit-speaker/${speaker.id}`">
                <button class="edit-btn">Edit</button>
              </router-link>
              <button @click="deleteSpeaker(speaker.id)" class="delete-btn">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";
import api from '@/api';

export default {
  name: "AdminSpeakerList",
  components: { AdminNavbar },
  data() {
    return {
      speakers: []
    };
  },
  mounted() {
    this.fetchSpeakers();
  },
  methods: {
    async fetchSpeakers() {
      try {
        const res = await api.get('/api/speakers');
        this.speakers = res.data;
      } catch (err) {
        alert('Failed to fetch speakers');
      }
    },
    async deleteSpeaker(id) {
      if (confirm('Are you sure you want to delete this speaker?')) {
        try {
          await api.delete(`/api/speakers/${id}`);
          this.fetchSpeakers();
        } catch (err) {
          alert('Failed to delete speaker');
        }
      }
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const d = new Date(dateString);
      return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' });
    }
  }
};
</script>

<style scoped>
.admin-speaker-list-page {
  min-height: 100vh;
  background: #f5f7fa;
}

.admin-form-container {
  max-width: 1100px;
  margin: 40px auto;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 6px 32px rgba(0,0,0,0.12);
  padding: 32px 24px 24px 24px;
}

h2 {
  margin-bottom: 24px;
  color: #1565C0;
  font-weight: 700;
  letter-spacing: 1px;
}

.submit-btn {
  background: #1976d2;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 22px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 18px;
  transition: background 0.2s;
  box-shadow: 0 2px 8px rgba(77,166,255,0.08);
}
.submit-btn:hover {
  background: #125ea2;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: #f9f9f9;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

.admin-table th, .admin-table td {
  padding: 13px 10px;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
}

.admin-table th {
  background: #1976d2;
  color: #fff;
  font-weight: 600;
  font-size: 15px;
}

.admin-table tr:last-child td {
  border-bottom: none;
}

.speaker-img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.10);
}

.edit-btn, .delete-btn {
  border: none;
  border-radius: 5px;
  padding: 7px 14px;
  margin: 0 3px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
}

.edit-btn {
  background: #43a047;
  color: #fff;
}
.edit-btn:hover {
  background: #357a38;
}

.delete-btn {
  background: #e53935;
  color: #fff;
}
.delete-btn:hover {
  background: #ab2020;
}

@media (max-width: 900px) {
  .admin-form-container {
    padding: 16px 6px;
  }
  .admin-table th, .admin-table td {
    padding: 8px 4px;
    font-size: 13px;
  }
  .speaker-img {
    width: 40px;
    height: 40px;
  }
}
</style>
