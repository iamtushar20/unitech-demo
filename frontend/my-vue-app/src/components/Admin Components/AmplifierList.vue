<template>
  <div class="amplifier-list-admin">
    <AdminNavbar />
    <div class="main-content">
      <h1>Power Amplifiers</h1>
      <button @click="showAddForm = true" class="add-button">Add New Amplifier</button>
      
      <div class="grid">
        <div v-for="amp in amplifiers" :key="amp.id" class="amp-card">
          <img v-if="amp.image_url" :src="amp.image_url" alt="Amplifier image" class="amp-image"/>
          <h3>{{ amp.model_name || 'Unnamed Amplifier' }}</h3>
          <p class="added-date">Added: {{ formatDate(amp.date_added) }}</p>
          
          <div class="specs-container">
            <!-- Power Output Specifications -->
            <div class="spec-section">
              <h4>Power Output</h4>
              <ul class="spec-list">
                <li v-if="amp.output_4ohm_stereo"><strong>Output 4Ω Stereo:</strong> {{ amp.output_4ohm_stereo }}</li>
                <li v-if="amp.output_8ohm_stereo"><strong>Output 8Ω Stereo:</strong> {{ amp.output_8ohm_stereo }}</li>
                <li v-if="amp.rated_power_stereo"><strong>Rated Power (Stereo):</strong> {{ amp.rated_power_stereo }}</li>
                <li v-if="amp.output_4ohm_bridge"><strong>Output 4Ω Bridge:</strong> {{ amp.output_4ohm_bridge }}</li>
                <li v-if="amp.output_8ohm_bridge"><strong>Output 8Ω Bridge:</strong> {{ amp.output_8ohm_bridge }}</li>
                <li v-if="amp.rated_power_bridge"><strong>Rated Power (Bridge):</strong> {{ amp.rated_power_bridge }}</li>
              </ul>
            </div>
            <!-- Audio Performance -->
            <div class="spec-section">
              <h4>Audio Performance</h4>
              <ul class="spec-list">
                <li v-if="amp.frequency_response"><strong>Frequency Response:</strong> {{ amp.frequency_response }}</li>
                <li v-if="amp.bandwidth"><strong>Bandwidth:</strong> {{ amp.bandwidth }}</li>
                <li v-if="amp.thd"><strong>THD+N:</strong> {{ amp.thd }}</li>
                <li v-if="amp.imd"><strong>IMD:</strong> {{ amp.imd }}</li>
                <li v-if="amp.sn_ratio"><strong>S/N Ratio:</strong> {{ amp.sn_ratio }}</li>
                <li v-if="amp.slew_rate"><strong>Slew Rate:</strong> {{ amp.slew_rate }}</li>
                <li v-if="amp.damping_factor"><strong>Damping Factor:</strong> {{ amp.damping_factor }}</li>
                <li v-if="amp.crosstalk"><strong>Crosstalk:</strong> {{ amp.crosstalk }}</li>
              </ul>
            </div>
            <!-- Input/Output -->
            <div class="spec-section">
              <h4>Input/Output</h4>
              <ul class="spec-list">
                <li v-if="amp.input_sensitivity_db"><strong>Input Sensitivity (dB):</strong> {{ amp.input_sensitivity_db }}</li>
                <li v-if="amp.input_sensitivity_v"><strong>Input Sensitivity (V):</strong> {{ amp.input_sensitivity_v }}</li>
                <li v-if="amp.input_impedance"><strong>Input Impedance:</strong> {{ amp.input_impedance }}</li>
                <li v-if="amp.input_connectors"><strong>Input Connectors:</strong> {{ amp.input_connectors }}</li>
                <li v-if="amp.input_cmr"><strong>Input CMRR:</strong> {{ amp.input_cmr }}</li>
                <li v-if="amp.output_circuitry"><strong>Output Circuitry:</strong> {{ amp.output_circuitry }}</li>
                <li v-if="amp.stereo_mode"><strong>Stereo Mode:</strong> {{ amp.stereo_mode }}</li>
                <li v-if="amp.filter_type"><strong>Filter Type:</strong> {{ amp.filter_type }}</li>
              </ul>
            </div>
            <!-- Power & Protection -->
            <div class="spec-section">
              <h4>Power & Protection</h4>
              <ul class="spec-list">
                <li v-if="amp.power_supply"><strong>Power Supply:</strong> {{ amp.power_supply }}</li>
                <li v-if="amp.power_consumption"><strong>Power Consumption:</strong> {{ amp.power_consumption }}</li>
                <li v-if="amp.fuse"><strong>Fuse:</strong> {{ amp.fuse }}</li>
                <li v-if="amp.smart_protections"><strong>Smart Protections:</strong> {{ amp.smart_protections }}</li>
                <li v-if="amp.indicators"><strong>Indicators:</strong> {{ amp.indicators }}</li>
                <li v-if="amp.technical"><strong>Technical Class:</strong> {{ amp.technical }}</li>
                <li v-if="amp.cooling"><strong>Cooling:</strong> {{ amp.cooling }}</li>
              </ul>
            </div>
            <!-- Physical -->
            <div class="spec-section">
              <h4>Physical</h4>
              <ul class="spec-list">
                <li v-if="amp.product_dimensions"><strong>Product Dimensions:</strong> {{ amp.product_dimensions }}</li>
                <li v-if="amp.packaging_dimensions"><strong>Packaging Dimensions:</strong> {{ amp.packaging_dimensions }}</li>
                <li v-if="amp.weight"><strong>Weight:</strong> {{ amp.weight }}</li>
                <li v-if="amp.product_gross_weight"><strong>Gross Weight:</strong> {{ amp.product_gross_weight }}</li>
              </ul>
            </div>
            <!-- Additional Info -->
            <div v-if="amp.extra_1 || amp.extra_2" class="spec-section">
              <h4>Additional Info</h4>
              <div v-if="amp.extra_1" class="additional-info">{{ amp.extra_1 }}</div>
              <div v-if="amp.extra_2" class="additional-info">{{ amp.extra_2 }}</div>
            </div>
          </div>
          <div class="actions">
            <button @click="editAmplifier(amp.id)" class="edit-btn">Edit</button>
            <button @click="deleteAmplifier(amp.id)" class="delete-btn">Delete</button>
          </div>
        </div>
      </div>

      <AddAmplifierForm 
        v-if="showAddForm"
        @close="showAddForm = false"
        @amplifier-added="fetchAmplifiers"
      />
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";
import AddAmplifierForm from './AddAmplifierForm.vue';
import api from '@/api';

export default {
  components: { AdminNavbar, AddAmplifierForm },
  data() {
    return {
      amplifiers: [],
      showAddForm: false
    };
  },
  mounted() {
    this.fetchAmplifiers();
  },
  methods: {
    async fetchAmplifiers() {
      try {
        const response = await api.get('/api/amplifiers');
        this.amplifiers = response.data;
      } catch (error) {
        console.error('Error fetching amplifiers:', error);
      }
    },
    editAmplifier(id) {
      this.$router.push(`/amplifiers/edit/${id}`);
    },
    async deleteAmplifier(id) {
      if (confirm('Are you sure you want to delete this amplifier?')) {
        try {
          await api.delete(`/api/amplifiers/${id}`);
          this.fetchAmplifiers();
        } catch (error) {
          console.error('Error deleting amplifier:', error);
        }
      }
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString();
    }
  }
};
</script>

<style scoped>
.amplifier-list-admin {
  min-height: 100vh;
  background: #f5f7fa;
}
.main-content {
  max-width: 1200px;
  margin: 40px auto 0;
  padding: 0 2vw 40px;
}
h1 {
  font-size: 2.2rem;
  color: #0c1b3a;
  margin-bottom: 16px;
  font-weight: 700;
  letter-spacing: -1px;
}
.add-button {
  background: #4da6ff;
  color: white;
  padding: 13px 30px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin: 18px 0 30px 0;
  font-weight: 600;
  font-size: 1.05rem;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(77,166,255,0.08);
}
.add-button:hover {
  background: #1565c0;
  box-shadow: 0 4px 18px rgba(77,166,255,0.13);
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(410px, 1fr));
  gap: 30px;
}
.amp-card {
  border: none;
  border-radius: 16px;
  padding: 26px 22px 22px 22px;
  background: #fff;
  box-shadow: 0 8px 30px rgba(12,27,58,0.07);
  transition: transform 0.2s, box-shadow 0.3s;
  position: relative;
}
.amp-card:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 0 14px 38px rgba(77,166,255,0.12);
}
.amp-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 18px;
  background: #e3e9f1;
}
h3 {
  margin-bottom: 8px;
  font-size: 1.45rem;
  color: #1565C0;
  font-weight: 600;
}
.added-date {
  color: #888;
  font-size: 0.93em;
  margin-bottom: 15px;
}
.specs-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 16px;
  margin-bottom: 18px;
}
.spec-section {
  margin-bottom: 8px;
}
.spec-section h4 {
  margin-bottom: 7px;
  padding-bottom: 4px;
  border-bottom: 1px solid #eaeaea;
  color: #424242;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.5px;
}
.spec-list {
  list-style: none;
  padding: 0;
  margin: 0 0 8px 0;
  font-size: 0.97em;
}
.spec-list li {
  margin-bottom: 4px;
  line-height: 1.4;
}
.spec-list strong {
  color: #1565C0;
  font-weight: 500;
}
.additional-info {
  font-size: 0.97em;
  color: #555;
  line-height: 1.4;
  margin-bottom: 5px;
}
.actions {
  margin-top: 16px;
  display: flex;
  gap: 12px;
}
.edit-btn { 
  background: #2196F3; 
  color: white; 
  border-radius: 6px;
}
.edit-btn:hover {
  background: #1565C0;
}
.delete-btn { 
  background: #f44336; 
  color: white; 
  border-radius: 6px;
}
.delete-btn:hover {
  background: #D32F2F;
}
button {
  padding: 8px 18px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
@media (max-width: 900px) {
  .main-content {
    padding: 0 1vw 30px;
  }
  .grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .specs-container {
    grid-template-columns: 1fr;
  }
}
</style>
