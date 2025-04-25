<template>
  <div class="landing-page">
    <!-- Navbar -->
    <nav class="navbar">
      <div class="logo-container">
        <img src="@/assets/logo.png" alt="UniTech Professional Audio" class="logo" />
      </div>
      <!-- Desktop Nav Links -->
      <ul class="nav-links" v-if="!isMobileMenuOpen">
        <li><router-link to="/user" class="nav-link" exact>Home</router-link></li>
        <li><router-link to="/speaker" class="nav-link">Speakers</router-link></li>
        <li><router-link to="/amplifier" class="nav-link active">Amplifiers</router-link></li>
        <li><router-link to="/microphone" class="nav-link">Microphones</router-link></li>
        <li><router-link to="/djmixer" class="nav-link">DJ Mixers</router-link></li>
      </ul>
      <!-- Hamburger Button -->
      <div class="mobile-menu-btn" @click="toggleMobileMenu">
        <span :class="{ open: isMobileMenuOpen }"></span>
        <span :class="{ open: isMobileMenuOpen }"></span>
        <span :class="{ open: isMobileMenuOpen }"></span>
      </div>
      <!-- Mobile Nav Overlay -->
      <transition name="fade">
        <div class="mobile-nav" v-if="isMobileMenuOpen">
          <button class="close-mobile-nav" @click="closeMobileMenu">&times;</button>
          <ul>
            <li><router-link to="/user" class="nav-link" @click="closeMobileMenu">Home</router-link></li>
            <li><router-link to="/speaker" class="nav-link" @click="closeMobileMenu">Speakers</router-link></li>
            <li><router-link to="/amplifier" class="nav-link active" @click="closeMobileMenu">Amplifiers</router-link></li>
            <li><router-link to="/microphone" class="nav-link" @click="closeMobileMenu">Microphones</router-link></li>
            <li><router-link to="/djmixer" class="nav-link" @click="closeMobileMenu">DJ Mixers</router-link></li>
          </ul>
        </div>
      </transition>
    </nav>

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
          <button class="slide-cta">Explore Now</button>
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

    <!-- Category Tabs -->
    <div class="category-filters">
      <div class="filter-title">
        <h2>Premium Amplifiers</h2>
        <p>Discover our collection of high-performance amplification solutions</p>
      </div>
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
      <div class="sort-options">
        <select class="sort-select">
          <option>Sort by: Featured</option>
          <option>Price: Low to High</option>
          <option>Price: High to Low</option>
          <option>Newest First</option>
        </select>
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

    <!-- Newsletter Subscription -->
    <div class="newsletter-section">
      <div class="newsletter-content">
        <h2>Stay Updated</h2>
        <p>Subscribe to our newsletter for exclusive deals and product updates</p>
        <div class="newsletter-form">
          <input type="email" placeholder="Your email address" class="newsletter-input" />
          <button class="newsletter-btn">Subscribe</button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="footer-content">
        <div class="footer-column">
          <h3>UniTech Audio</h3>
          <p>Premium audio solutions for professionals and enthusiasts. Quality sound that transforms experiences.</p>
          <div class="social-icons">
            <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-youtube"></i></a>
          </div>
        </div>
        <div class="footer-column">
          <h3>Quick Links</h3>
          <ul class="footer-links">
            <li><a href="#">About Us</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Support</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Blog</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Products</h3>
          <ul class="footer-links">
            <li><a href="#">Speakers</a></li>
            <li><a href="#">Amplifiers</a></li>
            <li><a href="#">Microphones</a></li>
            <li><a href="#">DJ Equipment</a></li>
            <li><a href="#">Accessories</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Contact Us</h3>
          <ul class="contact-info">
            <li><i class="fas fa-map-marker-alt"></i> 123 Audio Street, Sound City</li>
            <li><i class="fas fa-phone"></i> +1 (555) 123-4567</li>
            <li><i class="fas fa-envelope"></i> info@unitech-audio.com</li>
          </ul>
          <div class="payment-methods">
            <img src="https://via.placeholder.com/200x30" alt="Payment Methods" />
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 UniTech Professional Audio. All Rights Reserved.</p>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
          <a href="#">Sitemap</a>
        </div>
      </div>
    </footer>
  </div>
</template>


















<script>
// import axios from "axios";
import api from '@/api';
import AmplifierCard from "@/components/AmplifierCard.vue";

export default {
  name: "AmplifierCatalogue",
  components: { AmplifierCard },
  data() {
    return {
      isMobileMenuOpen: false,
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
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
      if (this.isMobileMenuOpen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false;
      document.body.style.overflow = '';
    },
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
  },
  beforeUnmount() {
    document.body.style.overflow = '';
  }
};
</script>



<style scoped>
  
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  
  @import url('https://fonts.googleapis.com/css2?family=Baskerville&display=swap');
  /* or another luxury font of your choice */
  
  .logo-container h3, 
  .footer-column h3:contains("UniTech") {
    font-family: 'Baskerville', serif;
    font-weight: 700;
    letter-spacing: 1px;
  }
  
  
  /* Enhanced Glassmorphism Navbar */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 32px 5%;
    background: rgba(5, 19, 44, 0.9);
    backdrop-filter: blur(10px);
    border-radius: 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  .logo-container {
    display: flex;
    align-items: center;
  }
  
  .logo {
    width: 180px;
    border-radius: 12px;
    transition: transform 0.3s ease;
  }
  
  .logo:hover {
    transform: scale(1.05);
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    align-items: center;
    gap: 30px;
    margin: 0;
    padding: 0;
  }
  
  .nav-link {
    color: white;
    text-decoration: none;
    font-weight: 500;
    font-size: 25px;
    padding: 20px 0;
    position: relative;
    transition: all 0.3s ease;
  }
  
  .nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: 0;
    left: 0;
    background-color: #4da6ff;
    transition: width 0.3s ease;
  }
  
  .nav-link:hover::after,
  .nav-link.active::after {
    width: 100%;
  }
  
  .nav-link:hover,
  .nav-link.active {
    color: #4da6ff;
  }
  
  
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

  
  .mobile-menu-btn {
    display: none;
    flex-direction: column;
    gap: 6px;
    cursor: pointer;
  }
  
  .mobile-menu-btn span {
    width: 30px;
    height: 3px;
    background: white;
    border-radius: 3px;
    transition: all 0.3s ease;
  }
  
  
  /* Mobile Nav Overlay Styles */
  .mobile-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(12, 27, 58, 0.97);
    backdrop-filter: blur(10px);
    z-index: 2000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    animation: fadeInMobileNav 0.3s;
  }
  @keyframes fadeInMobileNav {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  .mobile-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    width: 80%;
  }
  .mobile-nav li {
    margin: 20px 0;
    text-align: center;
  }
  .mobile-nav .nav-link,
  .mobile-nav .auth-btn {
    color: #fff;
    font-size: 1.5rem;
    font-weight: 600;
    background: none;
    border: none;
    margin: 0 auto;
    display: block;
    width: 100%;
    padding: 15px 0;
    transition: color 0.2s;
  }
  .mobile-nav .nav-link:hover,
  .mobile-nav .auth-btn:hover {
    color: #4da6ff;
  }
  .close-mobile-nav {
    position: absolute;
    top: 30px;
    right: 30px;
    font-size: 2.5rem;
    color: #fff;
    background: none;
    border: none;
    cursor: pointer;
    z-index: 1100;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  
  /* Responsive Design: Show/Hide Nav Elements */
  @media (max-width: 768px) {
    .nav-links,
    .auth-buttons {
      display: none;
    }
    .mobile-menu-btn {
      display: flex;
    }
  }
  /* Premium Hero Section */
  /* .hero-section {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 60px 5%;
    background: linear-gradient(135deg, #0c1b3a, #1a2a5f);
    color: white;
    position: relative;
    overflow: hidden;
  } */
  
  .hero-section {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 80px 5%;
    /* Only the image, no gradient */
    background: url('@/assets/background.png') center center/cover no-repeat;
    color: white;
    position: relative;
    overflow: hidden;
  }
  
  
  .hero-content {
    max-width: 600px;
    z-index: 1;
  }
  
  .badge-new {
    display: inline-block;
    background: #ff4d4d;
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 20px;
    box-shadow: 0 4px 10px rgba(255, 77, 77, 0.3);
  }
  
  .hero-content h1 {
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 20px;
  }
  
  .highlight {
    color: #4da6ff;
    position: relative;
  }
  
  .highlight::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 6px;
    background: rgba(77, 166, 255, 0.3);
    bottom: 5px;
    left: 0;
    z-index: -1;
  }
  
  .hero-content p {
    font-size: 1.1rem;
    margin-bottom: 30px;
    opacity: 0.9;
  }
  
  .buttons {
    display: flex;
    gap: 15px;
  }
  
  .shop-btn, .contact-btn {
    padding: 12px 28px;
    border: none;
    border-radius: 30px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .shop-btn {
    background: #4da6ff;
    color: white;
    box-shadow: 0 4px 15px rgba(77, 166, 255, 0.4);
  }
  
  .shop-btn:hover {
    background: #1a85ff;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(77, 166, 255, 0.5);
  }
  
  .contact-btn {
    background: transparent;
    color: white;
    border: 2px solid white;
  }
  
  .contact-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-3px);
  }
  
  .features {
    display: flex;
    gap: 25px;
    margin-top: 40px;
  }
  
  .feature-item {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .feature-item i {
    color: #4da6ff;
    font-size: 1.2rem;
  }
  
  .hero-image {
    position: relative;
    z-index: 1;
  }
  
  .main-image {
    max-width: 100%;
    border-radius: 20px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
    transition: transform 0.5s ease;
  }
  
  .main-image:hover {
    transform: scale(1.02);
  }
  
  .promo-tag {
    position: absolute;
    top: 20px;
    right: -10px;
    background: #ff4d4d;
    color: white;
    padding: 10px 20px;
    font-weight: 600;
    border-radius: 5px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  
  .promo-tag::after {
    content: '';
    position: absolute;
    right: 0;
    bottom: -10px;
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-top: 10px solid #cc0000;
  }
  
  /* Featured Categories */
  .featured-categories {
    padding: 80px 5%;
    background: #f8f9fa;
  }
  
  .featured-categories h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 50px;
    color: #0c1b3a;
  }
  
  .category-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
  }
  
  .category-card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  .category-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
  }
  
  .category-img {
    overflow: hidden;
  }
  
  .category-img img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  
  .category-card:hover .category-img img {
    transform: scale(1.1);
  }
  
  .category-card h3 {
    font-size: 1.3rem;
    margin: 20px 20px 10px;
    color: #0c1b3a;
  }
  
  .category-card p {
    font-size: 0.9rem;
    margin: 0 20px 20px;
    color: #666;
  }
  
  .category-link {
    display: inline-block;
    margin: 0 20px 20px;
    color: #4da6ff;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  
  .category-link:hover {
    color: #1a85ff;
  }
  
  /* Why Choose Us */
  .why-choose-us {
    padding: 80px 5%;
    background: #0c1b3a;
    color: white;
  }
  
  .section-header {
    text-align: center;
    margin-bottom: 50px;
  }
  
  .section-header h2 {
    font-size: 2.5rem;
    margin-bottom: 15px;
  }
  
  .section-header p {
    font-size: 1.1rem;
    opacity: 0.8;
  }
  
  .benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
  }
  
  .benefit-card {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 30px;
    text-align: center;
    transition: all 0.3s ease;
  }
  
  .benefit-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.2);
  }
  
  .benefit-icon {
    font-size: 2.5rem;
    color: #4da6ff;
    margin-bottom: 20px;
  }
  
  .benefit-card h3 {
    font-size: 1.3rem;
    margin-bottom: 15px;
  }
  
  .benefit-card p {
    font-size: 0.9rem;
    opacity: 0.8;
  }
  
  /* Testimonials */
  .testimonials {
    padding: 80px 5%;
    background: #f8f9fa;
  }
  
  .testimonial-slider {
    display: flex;
    gap: 30px;
    overflow-x: auto;
    padding: 20px 0;
  }
  
  .testimonial-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    min-width: 300px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }
  
  .testimonial-rating {
    color: #ffc107;
    font-size: 1.2rem;
    margin-bottom: 15px;
  }
  
  .testimonial-text {
    font-style: italic;
    margin-bottom: 20px;
  }
  
  .testimonial-author {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .author-img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .author-info h4 {
    font-size: 1.1rem;
    margin-bottom: 5px;
  }
  
  .author-info p {
    font-size: 0.9rem;
    color: #666;
  }
  
  /* Call to Action */
  .cta-section {
    padding: 80px 5%;
    background: linear-gradient(135deg, #0c1b3a, #1a2a5f);
    color: white;
    text-align: center;
  }
  
  .cta-content h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
  }
  
  .cta-content p {
    font-size: 1.1rem;
    margin-bottom: 30px;
    opacity: 0.9;
  }
  
  .cta-button {
    padding: 12px 30px;
    background: #4da6ff;
    color: white;
    border: none;
    border-radius: 30px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .cta-button:hover {
    background: #1a85ff;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(77, 166, 255, 0.5);
  }
  
  /* Newsletter Section */
  .newsletter-section {
    background: #f8f9fa;
    padding: 80px 5%;
    text-align: center;
  }
  
  .newsletter-content {
    max-width: 600px;
    margin: 0 auto;
  }
  
  .newsletter-content h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #0c1b3a;
  }
  
  .newsletter-content p {
    font-size: 1.1rem;
    margin-bottom: 30px;
    color: #666;
  }
  
  .newsletter-form {
    display: flex;
    gap: 10px;
  }
  
  .newsletter-input {
    flex-grow: 1;
    padding: 12px 20px;
    border: 1px solid #ddd;
    border-radius: 30px;
    font-size: 1rem;
  }
  
  .newsletter-btn {
    padding: 12px 30px;
    background: #4da6ff;
    color: white;
    border: none;
    border-radius: 30px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .newsletter-btn:hover {
    background: #1a85ff;
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(77, 166, 255, 0.5);
  }
  
  /* Footer Styles */
  .site-footer {
    background: #0c1b3a;
    color: #f0f2f5;
    padding: 60px 5% 30px;
  }
  
  .footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    margin-bottom: 40px;
  }
  
  .footer-column h3 {
    font-size: 1.2rem;
    margin-bottom: 20px;
    color: #4da6ff;
  }
  
  .footer-links {
    list-style: none;
    padding: 0;
  }
  
  .footer-links li {
    margin-bottom: 10px;
  }
  
  .footer-links a {
    color: #f0f2f5;
    text-decoration: none;
    transition: color 0.3s ease;
  }
  
  .footer-links a:hover {
    color: #4da6ff;
  }
  
  .social-icons {
    display: flex;
    gap: 15px;
    margin-top: 20px;
  }
  
  .social-icon {
    color: #f0f2f5;
    font-size: 1.2rem;
    transition: color 0.3s ease;
  }
  
  .social-icon:hover {
    color: #4da6ff;
  }
  
  .contact-info {
    list-style: none;
    padding: 0;
  }
  
  .contact-info li {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 15px;
  }
  
  .payment-methods img {
    max-width: 200px;
    margin-top: 20px;
  }
  
  .footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
  }
  
  .footer-bottom-links a {
    color: #f0f2f5;
    text-decoration: none;
    margin-left: 20px;
    transition: color 0.3s ease;
  }
  
  .footer-bottom-links a:hover {
    color: #4da6ff;
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .nav-links {
      display: none;
    }
  
    .mobile-menu-btn {
      display: flex;
    }
  
    .hero-section {
      flex-direction: column;
      text-align: center;
    }
  
    .hero-content {
      margin-bottom: 40px;
    }
  
    .features {
      justify-content: center;
    }
  
    .newsletter-form {
      flex-direction: column;
    }
  
    .footer-content {
      grid-template-columns: 1fr;
    }
  
    .footer-bottom {
      flex-direction: column;
      text-align: center;
    }
  
    .footer-bottom-links {
      margin-top: 20px;
    }
  
    .footer-bottom-links a {
      margin: 0 10px;
    }
  }
  
  
  .auth-buttons {
    display: flex;
    gap: 12px;
    margin-left: 20px;
  }
  
  .auth-btn {
    background: #4da6ff;
    color: #fff;
    border: none;
    border-radius: 30px;
    padding: 8px 22px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s;
    box-shadow: 0 4px 15px rgba(77,166,255,0.2);
  }
  .auth-btn:hover {
    background: #1a85ff;
  }
  

  /* Hamburger button styles */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
  z-index: 2100;
}
.mobile-menu-btn span {
  width: 30px;
  height: 3px;
  background: white;
  border-radius: 3px;
  transition: all 0.3s cubic-bezier(.68,-0.55,.27,1.55);
  display: block;
}
.mobile-menu-btn span.open:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}
.mobile-menu-btn span.open:nth-child(2) {
  opacity: 0;
}
.mobile-menu-btn span.open:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

/* Overlay Nav */
.mobile-nav {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(12, 27, 58, 0.97);
  backdrop-filter: blur(10px);
  z-index: 2000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  animation: fadeInMobileNav 0.3s;
}
@keyframes fadeInMobileNav {
  from { opacity: 0; }
  to { opacity: 1; }
}
.mobile-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 80%;
}
.mobile-nav li {
  margin: 20px 0;
  text-align: center;
}
.mobile-nav .nav-link {
  color: #fff;
  font-size: 1.5rem;
  font-weight: 600;
  background: none;
  border: none;
  margin: 0 auto;
  display: block;
  width: 100%;
  padding: 15px 0;
  transition: color 0.2s;
}
.mobile-nav .nav-link:hover {
  color: #4da6ff;
}
.close-mobile-nav {
  position: absolute;
  top: 30px;
  right: 30px;
  font-size: 2.5rem;
  color: #fff;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 2101;
}
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter, .fade-leave-to { opacity: 0; }

/* Responsive: show hamburger only on mobile */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .mobile-menu-btn { display: flex; }
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


/* Hamburger button styles */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 6px;
  cursor: pointer;
  z-index: 2100;
}
.mobile-menu-btn span {
  width: 30px;
  height: 3px;
  background: white;
  border-radius: 3px;
  transition: all 0.3s cubic-bezier(.68,-0.55,.27,1.55);
  display: block;
}
.mobile-menu-btn span.open:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}
.mobile-menu-btn span.open:nth-child(2) {
  opacity: 0;
}
.mobile-menu-btn span.open:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

/* Overlay Nav */
.mobile-nav {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(12, 27, 58, 0.97);
  backdrop-filter: blur(10px);
  z-index: 2000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  animation: fadeInMobileNav 0.3s;
}
@keyframes fadeInMobileNav {
  from { opacity: 0; }
  to { opacity: 1; }
}
.mobile-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 80%;
}
.mobile-nav li {
  margin: 20px 0;
  text-align: center;
}
.mobile-nav .nav-link {
  color: #fff;
  font-size: 1.5rem;
  font-weight: 700;
  background: none;
  border: none;
  margin: 0 auto;
  display: block;
  width: 100%;
  padding: 15px 0;
  transition: color 0.2s;
}
.mobile-nav .nav-link:hover {
  color: #4da6ff;
}
.close-mobile-nav {
  position: absolute;
  top: 30px;
  right: 30px;
  font-size: 2.5rem;
  color: #fff;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 2101;
}
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter, .fade-leave-to { opacity: 0; }

/* Responsive: show hamburger only on mobile */
@media (max-width: 900px) {
  .nav-links { display: none; }
  .mobile-menu-btn { display: flex; }
}
  
</style>