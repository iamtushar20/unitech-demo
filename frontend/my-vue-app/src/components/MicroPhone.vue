<template>
  <div class="product-page">
    <NavbarPage />

    <!-- Premium Hero Slideshow -->
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

    <!-- Hero Section -->
    <header class="hero-section">
      <div class="hero-content">
        <h1>Explore Our <span class="highlight">Microphones</span></h1>
        <p>Crystal-clear voice capture with premium quality microphones.</p>
      </div>
    </header>

    <NewsletterPage />
    <FooterPage />
  </div>
</template>

<script>
import NavbarPage from "@/components/NavbarPage.vue";
import NewsletterPage from "@/components/NewsletterPage.vue";
import FooterPage from "@/components/FooterPage.vue";

export default {
  name: "MicrophonePage",
  components: {
    NavbarPage,
    NewsletterPage,
    FooterPage
  },
  data() {
    return {
      currentSlide: 0,
      slides: [
        {
          image: require('@/assets/mic1.jpeg'),
          alt: "Premium Microphones",
          title: "Capture Every Nuance",
          description: "Discover our premium range of microphones for studio and stage"
        },
        {
          image: require('@/assets/mic2.jpeg'),
          alt: "Wireless Microphones",
          title: "Wireless Freedom",
          description: "Go cable-free with reliable wireless microphone solutions"
        },
        {
          image: require('@/assets/mic3.jpeg'),
          alt: "Podcasting",
          title: "Podcast Like a Pro",
          description: "Professional microphones for crystal-clear podcast audio"
        },
        {
          image: require('@/assets/mic4.jpeg'),
          alt: "Live Performance",
          title: "On-Stage Excellence",
          description: "Rugged microphones built for live performance"
        }
      ]
    };
  },
  methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.slides.length;
    },
    prevSlide() {
      this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    },
    goToSlide(index) {
      this.currentSlide = index;
    }
  },
  mounted() {
    setInterval(this.nextSlide, 6000);
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';
    document.head.appendChild(link);
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body {
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box;
}

.product-page {
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
  background: #f8f9fa;
  color: #333;
  line-height: 1.6;
  overflow-x: hidden;
}

/* Premium Slideshow Styling */
.slideshow-container {
  position: relative;
  max-width: 100%;
  margin: 25px auto;
  overflow: hidden;
  border-radius: 20px;
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

/* Navigation arrows */
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

.prev {
  left: 25px;
}

.next {
  right: 25px;
}

.prev:hover, .next:hover {
  background-color: rgba(0, 0, 0, 0.6);
  transform: translateY(-50%) scale(1.1);
}

/* Dots/indicators */
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

/* Hero Section */
.hero-section {
  margin: 60px 0 30px 0;
  text-align: center;
}
.hero-content h1 {
  font-size: 2.5rem;
  font-weight: 700;
}
.hero-content .highlight {
  color: #4da6ff;
}
.hero-content p {
  font-size: 1.2rem;
  color: #555;
}

/* Responsive Design */
@media (max-width: 768px) {
  .slide-content {
    left: 40px;
    bottom: 40px;
  }
  .slide-title {
    font-size: 2rem;
  }
  .slide-description {
    font-size: 1rem;
  }
}
</style>
