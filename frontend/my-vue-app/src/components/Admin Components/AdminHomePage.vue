<template>
  <div class="admin-landing-page">
    <!-- Admin Navbar -->
    <AdminNavbar />

    <!-- Admin Slideshow (copied and adapted from SpeakerPage.vue) -->
    <div class="slideshow-container">
      <div
        v-for="(slide, index) in slides"
        :key="index"
        class="slide"
        :class="{ 'active': currentSlide === index }"
      >
        <img :src="slide.image" :alt="slide.alt" />
        <div class="slide-content">
          <h2 class="slide-title">{{ slide.title }}</h2>
          <p class="slide-description">{{ slide.description }}</p>
        </div>
      </div>
      <a class="prev" @click="prevSlide"><i class="fas fa-chevron-left"></i></a>
      <a class="next" @click="nextSlide"><i class="fas fa-chevron-right"></i></a>
      <div class="dots-container">
        <span
          v-for="(slide, index) in slides"
          :key="`dot-${index}`"
          class="dot"
          :class="{ 'active': currentSlide === index }"
          @click="goToSlide(index)"
        ></span>
      </div>
    </div>

    <!-- Admin Quick Actions Section -->
    <section class="admin-quick-actions">
      <h2>Quick Actions</h2>
      <div class="action-grid">
        <router-link to="/admin/speakerslist" class="action-card">
          <i class="fas fa-bullhorn"></i>
          <h3>Manage Speakers</h3>
        </router-link>
        <div class="action-card" @click="$router.push('/admin/amplifierslist')">
          <i class="fas fa-plus"></i>
          <h3>Add Amplifier</h3>
        </div>
        <div class="action-card" @click="$router.push('#')">
          <i class="fas fa-plus"></i>
          <h3>Add Microphone</h3>
        </div>
        <div class="action-card" @click="$router.push('#')">
          <i class="fas fa-plus"></i>
          <h3>Add DJ Mixer</h3>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin Components/AdminNavbar.vue";

export default {
  name: "AdminHomePage",
  components: {
    AdminNavbar,
  },
  data() {
    return {
      currentSlide: 0,
      slides: [
        {
          image: require("@/assets/Speakers/img1.jpeg"),
          alt: "Premium Speakers",
          title: "Experience Sound Perfection",
          description: "Discover our premium range of high-fidelity speakers designed for audiophiles"
        },
        {
          image: require("@/assets/Speakers/img2.jpeg"),
          alt: "Professional Audio",
          title: "Professional-Grade Audio",
          description: "Studio-quality sound systems trusted by industry professionals worldwide"
        },
        {
          image: require("@/assets/Speakers/img3.jpeg"),
          alt: "Wireless Solutions",
          title: "Wireless Freedom",
          description: "Cutting-edge Bluetooth speakers with uncompromising sound quality"
        },
        {
          image: require("@/assets/Speakers/img4.jpeg"),
          alt: "Home Theater",
          title: "Transform Your Space",
          description: "Immersive audio solutions that elevate your home entertainment experience"
        },
      ],
    };
  },
  methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    },
    goToSlide(index) {
      this.currentSlide = index;
    },
  },
  mounted() {
    // Auto-slide every 6 seconds
    this.slideInterval = setInterval(this.nextSlide, 6000);

    // Add Font Awesome for icons if not globally included
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';
    document.head.appendChild(link);
  },
  beforeUnmount() {
    clearInterval(this.slideInterval);
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
.admin-landing-page {
  font-family: 'Poppins', sans-serif;
  background: #f8f9fa;
  color: #333;
  min-height: 100vh;
}

/* Slideshow Styling */
.slideshow-container {
  position: relative;
  max-width: 100%;
  margin: 0 auto;
  overflow: hidden;
  border-radius: 0;
  height: 500px;
  background: linear-gradient(135deg, #0c1b3a, #1a2a5f);
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.15);
}
.slide {
  display: none;
  width: 100%;
  height: 100%;
  position: relative;
}
.slide.active {
  display: block;
  animation: fadeZoom 1s ease;
}
@keyframes fadeZoom {
  from {
    opacity: 0.4;
    transform: scale(1.05);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
.slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.7);
}
.slide-content {
  position: absolute;
  bottom: 80px;
  left: 80px;
  max-width: 600px;
  color: white;
  text-align: left;
  animation: slideUp 1s ease;
}
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.slide-title {
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 15px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
.slide-description {
  font-size: 1.2rem;
  margin-bottom: 25px;
  line-height: 1.5;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 20px;
  transition: all 0.3s ease;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 10;
}
.prev { left: 25px; }
.next { right: 25px; }
.prev:hover, .next:hover {
  background-color: rgba(0, 0, 0, 0.6);
  transform: translateY(-50%) scale(1.1);
}
.dots-container {
  position: absolute;
  bottom: 30px;
  width: 100%;
  text-align: center;
  z-index: 10;
}
.dot {
  cursor: pointer;
  height: 12px;
  width: 12px;
  margin: 0 8px;
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 50%;
  display: inline-block;
  transition: all 0.3s ease;
}
.dot.active, .dot:hover {
  background-color: white;
  transform: scale(1.2);
}

/* Admin Quick Actions */
.admin-quick-actions {
  padding: 80px 5%;
  background: #0c1b3a;
  color: white;
}
.admin-quick-actions h2 {
  text-align: center;
  font-size: 2.2rem;
  margin-bottom: 40px;
  color: #4da6ff;
}
.action-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 30px;
  margin-top: 20px;
}
.action-card {
  background: white;
  color: #0c1b3a;
  border-radius: 15px;
  padding: 30px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  font-weight: 600;
  text-decoration: none;
}
.action-card:hover {
  transform: translateY(-5px);
  background: #4da6ff;
  color: white;
}
.action-card i {
  font-size: 2.5rem;
  margin-bottom: 15px;
}
.action-card h3 {
  margin: 0;
  font-size: 1.1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .slide-content {
    left: 20px;
    bottom: 30px;
    max-width: 90%;
  }
  .admin-quick-actions {
    padding: 50px 2%;
  }
  .action-grid {
    grid-template-columns: 1fr;
  }
}
</style>
