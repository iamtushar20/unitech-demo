<template>
  <div class="landing-page">
    <NavbarPage />

    <!-- Slideshow -->
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
          <!-- <button class="slide-cta">Explore Now</button> -->
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
    <div>
      <header class="hero-section">
      <div class="hero-content">
        <h1>Explore Our <span class="highlight">Premium Amplifiers</span></h1>
        <p>Discover our collection of high-performance amplification solutions</p>
      </div>
      </header>
    </div>

    <!-- Category Tabs -->
    <div class="category-filters">
      <!-- <header class="hero-section">
      <div class="hero-content">
        <h1>Explore Our <span class="highlight">Amplifiers</span></h1>
        <p>Discover our collection of high-performance amplification solutions</p>
      </div>
      </header> -->
      
        <!-- <h2>Premium Amplifiers</h2>
        <p></p> -->
      
      <div class="filter-options">
        <button
          class="filter-btn"
          :class="{ active: activeCategory === 'dual' }"
          @click="activeCategory = 'dual'"
        >Dual Channel</button>
        <button
          class="filter-btn"
          :class="{ active: activeCategory === 'multi' }"
          @click="activeCategory = 'multi'"
        >Multi Channel</button>
        <button
          class="filter-btn"
          :class="{ active: activeCategory === 'crossover' }"
          @click="activeCategory = 'crossover'"
        >Crossovers</button>
      </div>
      
    </div>

    <!-- Amplifier Cards (Dynamic, Full Width) -->
    <div v-if="activeCategory === 'dual'" class="amplifier-list">
      <AmplifierCard
        v-for="amp in dualChannelAmplifiers"
        :key="amp.id"
        :amplifier="amp"
      />
      <div v-if="dualChannelAmplifiers.length === 0" class="no-data">
        No dual channel amplifiers available.
      </div>
    </div>
    <div v-else-if="activeCategory === 'multi'" class="amplifier-list">
      <AmplifierCard
        v-for="amp in multiChannelAmplifiers"
        :key="amp.id"
        :amplifier="amp"
      />
      <div v-if="multiChannelAmplifiers.length === 0" class="no-data">
        No multi-channel amplifiers available.
      </div>
    </div>
    <div v-else-if="activeCategory === 'crossover'" class="amplifier-list">
      <AmplifierCard
        v-for="amp in crossoverAmplifiers"
        :key="amp.id"
        :amplifier="amp"
      />
      <div v-if="crossoverAmplifiers.length === 0" class="no-data">
        No crossover amplifiers available.
      </div>
    </div>

    <NewsletterPage />

    <FooterPage />
  </div>
</template>

<script>
import api from '@/api';
import AmplifierCard from "@/components/AmplifierCard.vue";
import NavbarPage from "@/components/NavbarPage.vue";
import NewsletterPage from "@/components/NewsletterPage.vue";
import FooterPage from "@/components/FooterPage.vue";

export default {
  name: "AmplifierCatalogue",
  components: { NavbarPage, NewsletterPage, FooterPage, AmplifierCard },
  data() {
    return {
      currentSlide: 0,
      activeCategory: 'dual',
      slides: [
        { 
          image: require("@/assets/amp1.jpeg"), 
          alt: "Premium Amplifiers", 
          title: "Powerful Sound Amplification",
          description: "Discover our premium range of high-performance amplifiers designed for professionals"
        },
        { 
          image: require("@/assets/amp2.jpeg"), 
          alt: "Dual Channel Amplifiers", 
          title: "Dual Channel Excellence",
          description: "Studio-quality amplification trusted by industry professionals worldwide"
        },
        { 
          image: require("@/assets/amp3.jpeg"), 
          alt: "Multi Channel Solutions", 
          title: "Multi-Channel Performance",
          description: "Versatile amplification solutions for complex audio setups and installations"
        },
        { 
          image: require("@/assets/amp4.jpeg"), 
          alt: "Crossover Systems", 
          title: "Precision Crossovers",
          description: "Advanced frequency management for optimized sound system performance"
        },
      ],
      amplifiers: [],
      loading: false,
      error: null,
    };
  },
  computed: {
    dualChannelAmplifiers() {
      return this.amplifiers.filter(amp => amp.extra_2 === "dual_channel");
    },
    multiChannelAmplifiers() {
      return this.amplifiers.filter(amp => amp.extra_2 === "multi_channel");
    },
    crossoverAmplifiers() {
      return this.amplifiers.filter(amp => amp.extra_2 === "crossover_");
    }
  },
  methods: {
    nextSlide() { this.currentSlide = (this.currentSlide + 1) % this.slides.length; },
    prevSlide() { this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length; },
    goToSlide(index) { this.currentSlide = index; }
  },
  async mounted() {
    this.loading = true;
    try {
      const { data } = await api.get("/api/amplifiers");
      this.amplifiers = data;
    } catch (err) {
      this.error = "Failed to load amplifiers.";
    } finally {
      this.loading = false;
    }
    setInterval(this.nextSlide, 6000);
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';
    document.head.appendChild(link);
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Baskerville&display=swap');

/* Only keep styles relevant to slideshow, category filters, amplifier cards, etc. */
/* Remove navbar, newsletter, and footer styles since they're now in their own components */

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
.slide-cta {
  background: #4da6ff;
  color: white;
  border: none;
  padding: 12px 28px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 1px;
  box-shadow: 0 4px 15px rgba(77, 166, 255, 0.4);
}
.slide-cta:hover {
  background: #1a85ff;
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(77, 166, 255, 0.5);
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
.prev { left: 25px; }
.next { right: 25px; }
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

/* Category Filters */
.category-filters {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 30px 5%;
  margin-top: 20px;
}
.filter-title h2 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 5px;
  color: #0c1b3a;
}
.filter-title p {
  color: #666;
  font-size: 1.1rem;
}
.filter-options {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}
.filter-btn {
  padding: 8px 16px;
  background: #f0f2f5;
  border: none;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  color: #333;
  cursor: pointer;
  transition: all 0.3s ease;
}
.filter-btn:hover,
.filter-btn.active {
  background: #4da6ff;
  color: white;
}
.sort-options {
  position: relative;
}
.sort-select {
  padding: 8px 16px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  font-size: 0.9rem;
  color: #333;
  background: white;
  cursor: pointer;
  appearance: none;
  padding-right: 30px;
}
.sort-options::after {
  content: '\25BC';
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}
.amplifier-list {
  width: 100%;
  max-width: 1200px;
  margin: 40px auto 0 auto;
  padding: 0 16px;
}
.no-data {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  padding: 60px 0;
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .slide-content {
    left: 20px;
    bottom: 30px;
    max-width: 90%;
  }
  .category-filters {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
  .filter-options {
    width: 100%;
    justify-content: flex-start;
  }
  .amplifier-list {
    padding: 0 4px;
  }
}
</style>
