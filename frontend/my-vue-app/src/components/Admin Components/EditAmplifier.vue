<template>
  <div class="edit-amplifier-admin">
    <AdminNavbar />
    <div class="edit-amplifier-container">
      <h1 v-if="amplifier">Edit Amplifier: {{ amplifier.model_name }}</h1>
      
      <div v-if="loading" class="loading-indicator">
        <p>Loading amplifier data...</p>
      </div>
      
      <div v-if="error" class="error-message">
        <p>{{ error }}</p>
        <button @click="$router.push('/amplifierslist')" class="back-btn">Back to List</button>
      </div>
      
      <AddAmplifierForm 
        v-if="amplifier && !loading && !error"
        :amplifier="amplifier"
        @close="$router.push('/amplifierslist')"
        @amplifier-added="handleSuccess"
      />
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";
import api from '@/api';
import AddAmplifierForm from './AddAmplifierForm.vue';

export default {
  components: { AdminNavbar, AddAmplifierForm },
  data() {
    return {
      amplifier: null,
      loading: true,
      error: null
    };
  },
  async created() {
    const ampId = this.$route.params.id;
    try {
      this.loading = true;
      const response = await api.get(`/api/amplifiers/${ampId}`);
      this.amplifier = {
        id: response.data.id,
        model_name: response.data.model_name,
        rated_power_stereo: response.data.rated_power_stereo,
        rated_power_bridge: response.data.rated_power_bridge,
        output_4ohm_stereo: response.data.output_4ohm_stereo,
        output_8ohm_stereo: response.data.output_8ohm_stereo,
        output_4ohm_bridge: response.data.output_4ohm_bridge,
        output_8ohm_bridge: response.data.output_8ohm_bridge,
        output_circuitry: response.data.output_circuitry,
        damping_factor: response.data.damping_factor,
        slew_rate: response.data.slew_rate,
        fuse: response.data.fuse,
        power_supply: response.data.power_supply,
        technical: response.data.technical,
        frequency_response: response.data.frequency_response,
        thd: response.data.thd,
        imd: response.data.imd,
        sn_ratio: response.data.sn_ratio,
        input_sensitivity_db: response.data.input_sensitivity_db,
        input_sensitivity_v: response.data.input_sensitivity_v,
        input_connectors: response.data.input_connectors,
        input_impedance: response.data.input_impedance,
        crosstalk: response.data.crosstalk,
        input_cmr: response.data.input_cmr,
        indicators: response.data.indicators,
        smart_protections: response.data.smart_protections,
        cooling: response.data.cooling,
        filter_type: response.data.filter_type,
        bandwidth: response.data.bandwidth,
        power_consumption: response.data.power_consumption,
        stereo_mode: response.data.stereo_mode,
        product_dimensions: response.data.product_dimensions,
        packaging_dimensions: response.data.packaging_dimensions,
        weight: response.data.weight,
        product_gross_weight: response.data.product_gross_weight,
        extra_1: response.data.extra_1,
        extra_2: response.data.extra_2,
        image_filename: response.data.image_filename,
        image_url: response.data.image_url,
      };
      document.title = `Edit Amplifier: ${this.amplifier.model_name || 'Unnamed'}`;
    } catch (error) {
      console.error('Error fetching amplifier:', error);
      this.error = 'Unable to load the amplifier. It may have been deleted or there was a network error.';
    } finally {
      this.loading = false;
    }
  },
  methods: {
    handleSuccess() {
      this.$toast?.success('Amplifier updated successfully!', {
        duration: 2000,
        onComplete: () => {
          this.$router.push('/amplifierslist');
        }
      }) || (alert('Amplifier updated successfully!'), this.$router.push('/amplifierslist'));
    }
  }
};
</script>

<style scoped>
.edit-amplifier-admin {
  min-height: 100vh;
  background: #f5f7fa;
}
.edit-amplifier-container {
  max-width: 900px;
  margin: 40px auto 0;
  padding: 32px 2vw 60px;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 8px 32px rgba(12,27,58,0.09);
}
h1 {
  font-size: 2rem;
  color: #0c1b3a;
  font-weight: 700;
  margin-bottom: 24px;
  letter-spacing: -1px;
}
.loading-indicator {
  text-align: center;
  padding: 40px 0;
  font-size: 1.1em;
  color: #666;
}
.error-message {
  background-color: #fff3f4;
  border: 1px solid #ffcdd2;
  border-radius: 6px;
  padding: 18px 20px;
  margin: 24px 0;
  color: #d32f2f;
  font-size: 1.08em;
  text-align: center;
}
.back-btn {
  background-color: #2196F3;
  color: white;
  border: none;
  padding: 10px 22px;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 18px;
  font-weight: 600;
  font-size: 1em;
  transition: background 0.2s;
}
.back-btn:hover {
  background: #1565C0;
}
@media (max-width: 800px) {
  .edit-amplifier-container {
    padding: 18px 2vw 36px;
    margin: 24px 0 0 0;
    border-radius: 0;
  }
  h1 { font-size: 1.2rem; }
}
</style>
