<template>
  <div class="speaker-card">
    <div class="speaker-image-container" @click="showModal = true">
      <img :src="image" :alt="name" class="speaker-image" />
    </div>
    <h2 class="product-title">{{ name }}</h2>
    <ul class="amp-details">
      <li v-if="magnetSize"><strong>Magnet Size:</strong> <span>{{ magnetSize }}</span></li>
      <li v-if="powerRating"><strong>Power Rating:</strong> <span>{{ powerRating }}</span></li>
      <li v-if="voiceCoilDiameter"><strong>Voice Coil Diameter:</strong> <span>{{ voiceCoilDiameter }}</span></li>
      <li v-if="voiceCoilType"><strong>Voice Coil Type:</strong> <span>{{ voiceCoilType }}</span></li>
    </ul>

    <!-- Fullscreen Image Modal -->
    <transition name="fade">
      <div v-if="showModal" class="fullscreen-modal" @click.self="showModal = false">
        <img :src="image" :alt="name" class="fullscreen-image" />
        <button class="close-btn" @click="showModal = false">&times;</button>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    magnetSize: String,
    powerRating: String,
    voiceCoilDiameter: String,
    voiceCoilType: String,
    image: String
  },
  data() {
    return {
      showModal: false
    };
  },
  watch: {
    showModal(newVal) {
      document.body.style.overflow = newVal ? 'hidden' : 'auto';
    }
  },
  mounted() {
    document.addEventListener('keydown', this.handleKeydown);
  },
  beforeUnmount() {
    document.removeEventListener('keydown', this.handleKeydown);
    document.body.style.overflow = 'auto';
  },
  methods: {
    handleKeydown(e) {
      if (e.key === 'Escape') {
        this.showModal = false;
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800&family=Inter:wght@400;600&display=swap');

.speaker-card {
  font-family: 'Inter', sans-serif;
  width: 220px;
  background: #f9fbfe;
  border-radius: 18px;
  box-shadow: 0 4px 24px rgba(44, 71, 130, 0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;
}

.speaker-image-container {
  width: 220px;
  height: 220px;
  background: #f0f2f5;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
}
.speaker-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  display: block;
  background: #fff;
  transition: transform 0.3s;
}
.speaker-image-container:hover .speaker-image {
  transform: scale(1.05);
}

.product-title {
  font-size: 1.6rem;
  font-weight: 800;
  text-align: center;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
  font-family: 'Orbitron', sans-serif;
  background: linear-gradient(90deg, #0f172a, #1e40af);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  position: relative;
}

.product-title::after {
  content: '';
  display: block;
  width: 80px;
  height: 2px;
  background: linear-gradient(to right, #3b82f6, #60a5fa);
  margin: 6px auto 0;
  border-radius: 1px;
}

.amp-details {
  list-style: none;
  padding: 0 16px 16px 16px;
  margin: 0;
  width: 100%;
  text-align: left;
  font-size: 0.9rem;
  color: #1e293b;
}
.amp-details li {
  display: flex;
  justify-content: space-between;
  padding: 4px 0;
  border-bottom: 1px dashed rgba(0, 0, 0, 0.05);
}
.amp-details li strong {
  font-weight: 600;
  color: #334155;
}
.amp-details li span {
  font-weight: 400;
  color: #0f172a;
}

/* Fullscreen Modal */
.fullscreen-modal {
  position: fixed;
  z-index: 9999;
  inset: 0;
  background: rgba(0, 0, 0, 0.92);
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
}
.fullscreen-image {
  max-width: 95vw;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 10px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}
.close-btn {
  position: absolute;
  top: 20px;
  right: 24px;
  background: transparent;
  border: none;
  font-size: 2.5rem;
  color: #fff;
  cursor: pointer;
}

/* Smooth fade and scale */
.fade-enter-active, .fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
