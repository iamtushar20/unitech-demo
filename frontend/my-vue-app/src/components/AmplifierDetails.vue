<template>
    <div class="amplifier-details-page">
      <NavbarPage />
  
      <!-- Product Section -->
      <div class="product-main">
        <div class="product-images">
          <img 
            :src="amplifier.image_url" 
            :alt="amplifier.model_name" 
            class="main-image" 
            v-if="amplifier.image_url" 
            @click="openImageModal(amplifier.image_url)"
          />
          <div class="thumbnail-row">
            <!-- First thumbnail from backend image -->
            <img 
              :src="amplifier.image_url" 
              class="thumbnail" 
              @click="openImageModal(amplifier.image_url)"
            />
            <!-- Second thumbnail from assets folder -->
            <img 
              :src="getLocalImage(amplifier.image_url)" 
              class="thumbnail" 
              @click="openImageModal(getLocalImage(amplifier.image_url))"
            />
          </div>
        </div>
        <div class="product-info">
          <h1 class="product-title">{{ dynamicHeading2 }}</h1>
        </div>
      </div>
  
      <!-- Image Modal -->
      <div v-if="isImageModalOpen" class="image-modal-overlay" @click.self="closeImageModal">
        <span class="image-modal-close" @click="closeImageModal">&times;</span>
        <img :src="modalImageSrc" class="image-modal-full" />
      </div>
  
      <!-- Tabs Section -->
      <div class="product-tabs">
        <button
          v-for="tab in tabs"
          :key="tab"
          :class="['tab-btn', { active: activeTab === tab }]"
          @click="activeTab = tab"
        >{{ tab }}</button>
      </div>
  
      <div class="tab-content">
        <!-- <div v-if="activeTab === 'Description'" class="p-6 bg-white rounded-xl shadow-md">
          <h2 class="text-2xl font-semibold text-gray-800 mb-4 border-b pb-2 border-gray-200">
            {{ dynamicHeading }}
          </h2>
          <ul class="space-y-3 list-disc list-inside text-gray-700 leading-relaxed">
            <li v-for="(point, index) in formattedExtra1" :key="index" class="pl-2">
              {{ point }}
            </li>
          </ul>
        </div> -->
        <div
            v-if="activeTab === 'Description'"
            class="p-8 bg-white rounded-2xl shadow-lg border border-gray-100 transition duration-300 ease-in-out"
        >
            <h2
            class="text-3xl font-bold text-gray-900 mb-6 border-b-2 pb-3 border-gray-200 tracking-wide"
            >
            {{ dynamicHeading }}
            </h2>

            <ul class="space-y-4 list-disc list-inside text-gray-700 text-lg leading-relaxed tracking-normal">
            <li
                v-for="(point, index) in formattedExtra1"
                :key="index"
                class="pl-2 hover:text-gray-900 transition-colors duration-200"
            >
                {{ point }}
            </li>
            </ul>
        </div>
  
        <div v-else-if="activeTab === 'Specifications'">
          <table class="specs-table">
            <tr v-for="(spec, index) in dynamicSpecs" :key="index">
              <th>{{ spec.label }}</th>
              <td>{{ spec.value }}</td>
            </tr>
          </table>
        </div>
      </div>
  
      <NewsletterPage />
      <FooterPage />
    </div>
  </template>
  
  <script>
  import api from '@/api';
  import NavbarPage from '@/components/NavbarPage.vue';
  import FooterPage from '@/components/FooterPage.vue';
  import NewsletterPage from '@/components/NewsletterPage.vue';
  
  export default {
    name: "AmplifierDetails",
    components: {
      NavbarPage,
      FooterPage,
      NewsletterPage
    },
    data() {
      return {
        amplifier: {},
        activeTab: 'Description',
        tabs: ['Description', 'Specifications'],
        isImageModalOpen: false,
        modalImageSrc: null,
      };
    },
    computed: {
      formattedExtra1() {
        return this.amplifier.extra_1
          ? this.amplifier.extra_1.split('.').map(p => p.trim()).filter(p => p)
          : [];
      },
      dynamicHeading() {
        const modelPrefix = this.amplifier.model_name?.split('-')[0] || 'TD';
        const typeMap = {
          dual_channel: 'Dual Channel Power Amplifier',
          multi_channel: 'Multi Channel Power Amplifier',
          crossover_: 'Crossover Power Amplifier'
        };
        const type = typeMap[this.amplifier.extra_2] || 'Power Amplifier';
        return `${modelPrefix} Series – ${type}`;
      },
      dynamicHeading2() {
        const modelPrefix = this.amplifier.model_name;
        const typeMap = {
          dual_channel: 'Dual Channel Power Amplifier',
          multi_channel: 'Multi Channel Power Amplifier',
          crossover_: 'Crossover Power Amplifier'
        };
        const type = typeMap[this.amplifier.extra_2] || 'Power Amplifier';
        return `${modelPrefix} – ${type}`;
      },
      dynamicSpecs() {
        const specFields = [
          { label: "Model", key: "model_name" },
          { label: "Rated Power (Stereo)", key: "rated_power_stereo" },
          { label: "Rated Power (Bridge)", key: "rated_power_bridge" },
          { label: "Output Circuitry", key: "output_circuitry" },
          { label: "Frequency Response", key: "frequency_response" },
          { label: "S/N Ratio", key: "sn_ratio" },
          { label: "Damping Factor", key: "damping_factor" },
          { label: "Input Sensitivity (dB)", key: "input_sensitivity_db" },
          { label: "Input Sensitivity (V)", key: "input_sensitivity_v" },
          { label: "Input Impedance", key: "input_impedance" },
          { label: "Smart Protections", key: "smart_protections" },
          { label: "Product Dimensions", key: "product_dimensions" },
          { label: "Weight", key: "weight" },
          { label: "Output 4Ω Stereo", key: "output_4ohm_stereo" },
          { label: "Output 8Ω Stereo", key: "output_8ohm_stereo" },
          { label: "Output 4Ω Bridge", key: "output_4ohm_bridge" },
          { label: "Output 8Ω Bridge", key: "output_8ohm_bridge" },
          { label: "Slew Rate", key: "slew_rate" },
          { label: "Fuse", key: "fuse" },
          { label: "Power Supply", key: "power_supply" },
          { label: "THD", key: "thd" },
          { label: "IMD", key: "imd" },
          { label: "Input Connectors", key: "input_connectors" },
          { label: "Crosstalk", key: "crosstalk" },
          { label: "Input CMR", key: "input_cmr" },
          { label: "Indicators", key: "indicators" },
          { label: "Cooling", key: "cooling" },
          { label: "Filter Type", key: "filter_type" },
          { label: "Bandwidth", key: "bandwidth" },
          { label: "Power Consumption", key: "power_consumption" },
          { label: "Stereo Mode", key: "stereo_mode" },
          { label: "Packaging Dimensions", key: "packaging_dimensions" },
          { label: "Gross Weight", key: "product_gross_weight" }
        ];
        return specFields
          .map(spec => ({
            label: spec.label,
            value: this.amplifier[spec.key]
          }))
          .filter(spec => spec.value && spec.value.trim() !== "");
      }
    },
    methods: {
      openImageModal(src) {
        this.modalImageSrc = src;
        this.isImageModalOpen = true;
        document.body.style.overflow = 'hidden';
      },
      closeImageModal() {
        this.isImageModalOpen = false;
        this.modalImageSrc = null;
        document.body.style.overflow = '';
      },
      getLocalImage(imageUrl) {
        if (!imageUrl) return '';
        const filename = imageUrl.split('/').pop(); // Extracts filename from full URL
        try {
          return require(`@/assets/amplifiers/second/${filename}`);
        } catch (e) {
          console.warn(`Image not found in local assets for ${filename}`);
          return '';
        }
      }
    },
    async mounted() {
      try {
        const { data } = await api.get(`/api/amplifiers/${this.$route.params.id}`);
        this.amplifier = data;
      } catch (err) {
        console.error('Error fetching amplifier data:', err);
      }
    },
    beforeUnmount() {
      document.body.style.overflow = '';
    }
  };
  </script>
  
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet');

  
  .amplifier-details-page {
    background: #f8f9fa;
    min-height: 100vh;
  }

  .product-main {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 48px;
    max-width: 1200px;
    margin: 40px auto 0 auto;
    padding: 40px 5%;
    background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
    border-radius: 20px;
    box-shadow: 0 8px 40px rgba(44, 62, 80, 0.08);
  }

  .product-images {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .main-image {
    width: 100%;
    max-width: 420px;
    height: 220px;
    object-fit: contain;
    border-radius: 14px;
    margin-bottom: 18px;
    background: #f0f2f5;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
    transition: transform 0.3s ease;
  }

  .main-image:hover {
    transform: scale(1.03);
  }

  .thumbnail-row {
    display: flex;
    gap: 10px;
    justify-content: center;
  }

  .thumbnail {
    width: 70px;
    height: 45px;
    object-fit: contain;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    background: #fff;
    cursor: pointer;
  }

  .product-info {
    flex: 1.2;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  .product-title {
  font-size: 2.8rem;
  font-weight: 800;
  text-align: center;
  line-height: 1.3;
  letter-spacing: -0.5px;
  background: linear-gradient(90deg, #0f172a, #1e40af);
  -webkit-background-clip: text;
  background-clip: text; /* ✅ Standard property for non-WebKit browsers */
  -webkit-text-fill-color: transparent;
  color: transparent;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  position: relative;
  margin-top: 1rem;
  margin-bottom: 1.5rem;
  /* font-family: 'Poppins', 'Segoe UI', sans-serif; */
  font-family: 'Orbitron', 'Segoe UI', sans-serif;

}

.product-title::after {
  content: '';
  display: block;
  width: 120px;
  height: 3px;
  margin: 12px auto 0;
  background: linear-gradient(90deg, #2563eb, #60a5fa);
  border-radius: 3px;
  transition: width 0.3s ease-in-out;
}

.product-title:hover::after {
  width: 160px;
}

/* Optional glow effect on hover for ultra-premium feel */
.product-title:hover {
  text-shadow: 0 0 10px rgba(96, 165, 250, 0.4), 0 0 20px rgba(96, 165, 250, 0.2);
}
  .image-modal-overlay {
    position: fixed;
    z-index: 9999;
    left: 0; top: 0; right: 0; bottom: 0;
    width: 100vw; height: 100vh;
    background: rgba(0,0,0,0.85);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.2s;
  }

  .image-modal-full {
    max-width: 90vw;
    max-height: 80vh;
    border-radius: 10px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5);
    background: #fff;
  }

  .image-modal-close {
    position: absolute;
    top: 32px;
    right: 48px;
    font-size: 3rem;
    color: #fff;
    cursor: pointer;
    font-weight: bold;
    z-index: 10001;
    text-shadow: 0 2px 12px #000;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }

  .product-tabs {
    display: flex;
    gap: 24px;
    max-width: 1200px;
    margin: 36px auto 0 auto;
    padding: 0 5%;
  }

  .tab-btn {
    background: #f0f2f5;
    border: none;
    border-radius: 18px 18px 0 0;
    padding: 14px 38px;
    font-size: 1.1rem;
    font-weight: 600;
    color: #222;
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
  }

  .tab-btn.active {
    background: #4da6ff;
    color: #fff;
  }

  .tab-content {
    background: #fff;
    max-width: 1200px;
    margin: 0 auto 40px auto;
    padding: 36px 5%;
    border-radius: 0 0 18px 18px;
    box-shadow: 0 6px 30px rgba(44, 62, 80, 0.07);
    font-size: 1.08rem;
  }

  .specs-table {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 0;
    width: 100%;
    margin-top: 20px;
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  }

  .specs-table tr {
    display: contents;
  }

  .specs-table th,
  .specs-table td {
    padding: 16px;
    background: #f9fafb;
    border-bottom: 1px solid #eee;
    font-size: 1rem;
  }

  .specs-table th {
    font-weight: 600;
    color: #334155;
    background: #eef3f7;
  }

  .specs-table td {
    color: #475569;
    background: #fff;
  }

  .specs-table td:hover,
  .specs-table th:hover {
    background: #f1f5f9;
  }

  @media (max-width: 900px) {
    .product-main {
      flex-direction: column;
      padding: 24px 5%;
      gap: 28px;
      align-items: center;
      text-align: center;
    }

    .main-image {
      width: 100%;
      max-width: 320px;
      height: 180px;
      margin: 0 auto 18px auto;
    }

    .thumbnail-row {
      justify-content: center;
    }

    .product-title {
      text-align: center;
    }

    .product-tabs {
      justify-content: center;
      padding: 0 5%;
      flex-wrap: wrap;
    }

    .tab-btn {
      padding: 10px 20px;
      font-size: 1rem;
    }

    .tab-content {
      padding: 20px 5%;
    }

    .specs-table th {
      width: 40%;
    }
  }

  @media (max-width: 768px) {
    .specs-table {
      display: block;
    }

    .specs-table tr {
      display: block;
      margin-bottom: 12px;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 1px 6px rgba(0, 0, 0, 0.03);
    }

    .specs-table th,
    .specs-table td {
      display: block;
      width: 100%;
      padding: 12px 16px;
    }

    .specs-table th {
      background: #f1f5f9;
      border-bottom: none;
      font-size: 0.95rem;
      color: #475569;
    }

    .specs-table td {
      background: #fff;
      font-size: 1.05rem;
      font-weight: 500;
    }
  }
</style>
