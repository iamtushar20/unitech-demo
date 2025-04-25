<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-form">
      <h2>{{ isEditing ? 'Edit Amplifier' : 'Add New Amplifier' }}</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-tabs">
          <button 
            type="button" 
            v-for="(tab, index) in tabs" 
            :key="index"
            :class="['tab-button', { active: activeTab === index }]"
            @click="activeTab = index"
          >
            {{ tab }}
          </button>
        </div>
        
        <div class="form-grid" v-if="activeTab === 0">
          <div class="form-group full-width">
            <label for="model_name">Model Name</label>
            <input type="text" v-model="formData.model_name" id="model_name" required autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="output_circuitry">Output Circuitry</label>
            <input type="text" v-model="formData.output_circuitry" id="output_circuitry" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="technical">Technical Class</label>
            <input type="text" v-model="formData.technical" id="technical" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 1">
          <div class="form-group">
            <label for="output_4ohm_stereo">Output 4Ω Stereo</label>
            <input type="text" v-model="formData.output_4ohm_stereo" id="output_4ohm_stereo" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="output_8ohm_stereo">Output 8Ω Stereo</label>
            <input type="text" v-model="formData.output_8ohm_stereo" id="output_8ohm_stereo" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="output_4ohm_bridge">Output 4Ω Bridge</label>
            <input type="text" v-model="formData.output_4ohm_bridge" id="output_4ohm_bridge" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="output_8ohm_bridge">Output 8Ω Bridge</label>
            <input type="text" v-model="formData.output_8ohm_bridge" id="output_8ohm_bridge" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="rated_power_stereo">Rated Power (Stereo)</label>
            <input type="text" v-model="formData.rated_power_stereo" id="rated_power_stereo" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="rated_power_bridge">Rated Power (Bridge)</label>
            <input type="text" v-model="formData.rated_power_bridge" id="rated_power_bridge" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 2">
          <div class="form-group">
            <label for="frequency_response">Frequency Response</label>
            <input type="text" v-model="formData.frequency_response" id="frequency_response" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="bandwidth">Bandwidth</label>
            <input type="text" v-model="formData.bandwidth" id="bandwidth" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="sn_ratio">S/N Ratio</label>
            <input type="text" v-model="formData.sn_ratio" id="sn_ratio" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="thd">THD+N</label>
            <input type="text" v-model="formData.thd" id="thd" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="imd">IMD</label>
            <input type="text" v-model="formData.imd" id="imd" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="damping_factor">Damping Factor</label>
            <input type="text" v-model="formData.damping_factor" id="damping_factor" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="slew_rate">Slew Rate</label>
            <input type="text" v-model="formData.slew_rate" id="slew_rate" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="crosstalk">Crosstalk</label>
            <input type="text" v-model="formData.crosstalk" id="crosstalk" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 3">
          <div class="form-group">
            <label for="input_sensitivity_db">Input Sensitivity (dB)</label>
            <input type="text" v-model="formData.input_sensitivity_db" id="input_sensitivity_db" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="input_sensitivity_v">Input Sensitivity (V)</label>
            <input type="text" v-model="formData.input_sensitivity_v" id="input_sensitivity_v" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="input_impedance">Input Impedance</label>
            <input type="text" v-model="formData.input_impedance" id="input_impedance" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="input_connectors">Input Connectors</label>
            <input type="text" v-model="formData.input_connectors" id="input_connectors" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="input_cmr">Input CMRR</label>
            <input type="text" v-model="formData.input_cmr" id="input_cmr" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="stereo_mode">Stereo Mode</label>
            <input type="text" v-model="formData.stereo_mode" id="stereo_mode" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 4">
          <div class="form-group">
            <label for="power_supply">Power Supply</label>
            <input type="text" v-model="formData.power_supply" id="power_supply" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="power_consumption">Power Consumption</label>
            <input type="text" v-model="formData.power_consumption" id="power_consumption" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="fuse">Fuse</label>
            <input type="text" v-model="formData.fuse" id="fuse" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="smart_protections">Smart Protections</label>
            <input type="text" v-model="formData.smart_protections" id="smart_protections" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="indicators">Indicators</label>
            <input type="text" v-model="formData.indicators" id="indicators" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="cooling">Cooling</label>
            <input type="text" v-model="formData.cooling" id="cooling" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="filter_type">Filter Type</label>
            <input type="text" v-model="formData.filter_type" id="filter_type" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 5">
          <div class="form-group">
            <label for="product_dimensions">Product Dimensions (mm)</label>
            <input type="text" v-model="formData.product_dimensions" id="product_dimensions" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="packaging_dimensions">Packaging Dimensions (mm)</label>
            <input type="text" v-model="formData.packaging_dimensions" id="packaging_dimensions" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="weight">Weight</label>
            <input type="text" v-model="formData.weight" id="weight" autocomplete="off" />
          </div>
          
          <div class="form-group">
            <label for="product_gross_weight">Product Gross Weight</label>
            <input type="text" v-model="formData.product_gross_weight" id="product_gross_weight" autocomplete="off" />
          </div>
        </div>

        <div class="form-grid" v-if="activeTab === 6">
          <div class="form-group">
            <label for="extra_1">Additional Notes 1</label>
            <textarea v-model="formData.extra_1" id="extra_1" rows="3" autocomplete="off"></textarea>
          </div>
          
          <div class="form-group">
            <label for="extra_2">Additional Notes 2</label>
            <textarea v-model="formData.extra_2" id="extra_2" rows="3" autocomplete="off"></textarea>
          </div>
          
          <div class="form-group full-width">
            <label>Image</label>
            <input type="file" @change="handleImageUpload" accept="image/*"/>
            <div v-if="formData.image_url" class="image-preview">
              <img :src="formData.image_url" alt="Amplifier Image" />
            </div>
          </div>
        </div>

        <div class="modal-actions">
          <button type="submit" class="submit-btn">
            {{ isEditing ? 'Update' : 'Create' }}
          </button>
          <button type="button" @click="$emit('close')" class="cancel-btn">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import api from '@/api'; // Use your Axios instance!

export default {
  props: {
    amplifier: { type: Object, default: null }
  },
  data() {
    return {
      formData: {},
      imageFile: null,
      activeTab: 0,
      tabs: [
        'Basic Info',
        'Power Output',
        'Audio Performance',
        'Input/Output',
        'Power & Protection',
        'Physical',
        'Additional'
      ]
    };
  },
  computed: {
    isEditing() {
      return !!this.amplifier;
    }
  },
  created() {
    if (this.amplifier) {
      this.formData = { ...this.amplifier };
    }
  },
  methods: {
    handleImageUpload(e) {
      this.imageFile = e.target.files[0];
      // Show preview for new image
      if (this.imageFile) {
        const reader = new FileReader();
        reader.onload = e => {
          this.formData.image_url = e.target.result;
        };
        reader.readAsDataURL(this.imageFile);
      }
    },
    async handleSubmit() {
      const formData = new FormData();

      Object.entries(this.formData).forEach(([key, value]) => {
        if (value !== null && value !== undefined && key !== 'image_url') {
          formData.append(key, value);
        }
      });

      if (this.imageFile) {
        formData.append('image', this.imageFile);
      }

      try {
        const url = this.isEditing 
          ? `/api/amplifiers/${this.amplifier.id}`
          : `/api/amplifiers`;

        const method = this.isEditing ? 'put' : 'post';

        await api[method](url, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });

        this.$emit('amplifier-added');
        this.$emit('close');
      } catch (error) {
        console.error('Error saving amplifier:', error);
      }
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(30, 42, 70, 0.25);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-form {
  background: #fff;
  border-radius: 14px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.18);
  padding: 32px 30px 24px 30px;
  min-width: 340px;
  max-width: 720px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  animation: fadeIn 0.2s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.98);}
  to { opacity: 1; transform: scale(1);}
}

h2 {
  color: #1976d2;
  font-weight: 700;
  letter-spacing: 1px;
  text-align: center;
  margin-bottom: 22px;
}

.form-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
  border-bottom: 1px solid #e1e4e8;
  padding-bottom: 10px;
}

.tab-button {
  background: none;
  border: none;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  color: #586069;
  transition: all 0.2s;
}

.tab-button:hover {
  background: #f0f3f6;
  color: #1976d2;
}

.tab-button.active {
  background: #1976d2;
  color: white;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px 18px;
  margin-bottom: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.full-width {
  grid-column: 1 / -1;
}

label {
  margin-bottom: 6px;
  color: #2c3e50;
  font-size: 15px;
  font-weight: 600;
}

input[type="text"],
input[type="number"],
input[type="file"],
textarea {
  padding: 8px 10px;
  border: 1px solid #d0d0d0;
  border-radius: 6px;
  font-size: 15px;
  background: #f8fafd;
  transition: border 0.2s;
}

textarea {
  resize: vertical;
  min-height: 80px;
}

input:focus, textarea:focus {
  border-color: #1976d2;
  outline: none;
}

.image-preview {
  margin-top: 8px;
}
.image-preview img {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 7px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.10);
  border: 1px solid #e0e0e0;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 10px;
}

.submit-btn {
  background: #1976d2;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 28px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.submit-btn:hover {
  background: #125ea2;
}

.cancel-btn {
  background: #f44336;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 24px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.cancel-btn:hover {
  background: #b71c1c;
}

@media (max-width: 650px) {
  .modal-form {
    padding: 16px 12px;
    min-width: unset;
    max-width: 98vw;
  }
  .form-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .tab-button {
    font-size: 12px;
    padding: 6px 10px;
  }
}
</style>
