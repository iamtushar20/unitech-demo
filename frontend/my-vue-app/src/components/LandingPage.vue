<template>
  <div class="landing-page">
    <!-- Use NavbarPage component instead of inline navbar -->
    <NavbarPage />

    <!-- LOGIN & REGISTER MODALS -->
    <LoginForm
      v-if="showLogin"
      @close="showLogin = false"
      @switch-to-register="openRegister"
    />
    <RegisterForm
      v-if="showRegister"
      @close="showRegister = false"
      @switch-to-login="openLogin"
    />

    <!-- Premium Hero Section -->
    <header class="hero-section">
      <div class="hero-content">
        <h1>
          <span class="glitter-logo">UniTech</span><br>
          <span class="professional-audio">Professional <br></span>
          <span class="rotating-text"></span>
        </h1>
        <p>Experience crystal-clear audio with our high-quality speakers, amplifiers, microphones, and DJ mixers designed for professionals and enthusiasts.</p>
        <div class="buttons">
          <router-link to="/speaker"><button class="shop-btn">Shop Speakers</button></router-link>
          <router-link to="/contact"><button class="contact-btn">Contact Us</button></router-link>
        </div>
        <div class="features">
          <div class="feature-item">
            <i class="fas fa-shield-alt"></i>
            <span>3-Year Warranty</span>
          </div>
          <div class="feature-item">
            <i class="fas fa-certificate"></i>
            <span>Authentic Products</span>
          </div>
          <div class="feature-item">
            <i class="fas fa-tools"></i>
            <span>Free Installation</span>
          </div>
        </div>
      </div>
    </header>

    <!-- Featured Categories -->
    <section class="featured-categories">
      <h2>Browse Our Categories</h2>
      <div class="category-grid">
        <div class="category-card">
          <div class="category-img">
            <img src="@/assets/speaker_final.png" alt="Speakers" />
          </div>
          <h3>Speakers</h3>
          <p>Premium sound quality for every space</p>
          <router-link to="/speaker" class="category-link">Explore <i class="fas fa-arrow-right"></i></router-link>
        </div>
        <div class="category-card">
          <div class="category-img">
            <img src="@/assets/amplifier_final.jpeg" alt="Amplifiers" />
          </div>
          <h3>Amplifiers</h3>
          <p>Powerful amplification for clear sound</p>
          <router-link to="/amplifier" class="category-link">Explore <i class="fas fa-arrow-right"></i></router-link>
        </div>
        <div class="category-card">
          <div class="category-img">
            <img src="@/assets/microphone_final.jpeg" alt="Microphones" />
          </div>
          <h3>Microphones</h3>
          <p>Crystal clear voice capture technology</p>
          <router-link to="/microphone" class="category-link">Explore <i class="fas fa-arrow-right"></i></router-link>
        </div>
        <div class="category-card">
          <div class="category-img">
            <img src="@/assets/djmixer_final.jpeg" alt="DJ Mixers" />
          </div>
          <h3>DJ Mixers</h3>
          <p>Professional mixing equipment</p>
          <router-link to="/djmixer" class="category-link">Explore <i class="fas fa-arrow-right"></i></router-link>
        </div>
      </div>
    </section>

    <!-- Why Choose Us -->
    <section class="why-choose-us">
      <div class="section-header">
        <h2>Why Choose UniTech Audio</h2>
        <p>We're dedicated to providing the best audio solutions for professionals and enthusiasts</p>
      </div>
      <div class="benefits-grid">
        <div class="benefit-card">
          <div class="benefit-icon">
            <i class="fas fa-headphones"></i>
          </div>
          <h3>Premium Quality</h3>
          <p>All our products are sourced from top manufacturers and undergo rigorous quality testing</p>
        </div>
        <div class="benefit-card">
          <div class="benefit-icon">
            <i class="fas fa-truck"></i>
          </div>
          <h3>Fast Delivery</h3>
          <p>Enjoy quick and reliable shipping options to get your equipment when you need it</p>
        </div>
        <div class="benefit-card">
          <div class="benefit-icon">
            <i class="fas fa-comments"></i>
          </div>
          <h3>Expert Support</h3>
          <p>Our team of audio professionals is always ready to help with setup and troubleshooting</p>
        </div>
        <div class="benefit-card">
          <div class="benefit-icon">
            <i class="fas fa-sync-alt"></i>
          </div>
          <h3>Easy Returns</h3>
          <p>Not satisfied? Return within 30 days for a full refund or exchange</p>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials">
      <div class="section-header">
        <h2>What Our Customers Say</h2>
        <p>Trusted by professionals and audio enthusiasts worldwide</p>
      </div>
      <div class="testimonial-slider">
        <div class="testimonial-card">
          <div class="testimonial-rating">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
          </div>
          <p class="testimonial-text">"The sound quality of the X-Bass 2000 speakers is incredible. I've been using them for my studio and the clarity is unmatched. Highly recommended!"</p>
          <div class="testimonial-author">
            <img src="https://via.placeholder.com/60x60" alt="Customer" class="author-img" />
            <div class="author-info">
              <h4>Michael Johnson</h4>
              <p>Music Producer</p>
            </div>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="testimonial-rating">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
          </div>
          <p class="testimonial-text">"UniTech's customer service is exceptional. They helped me select the perfect DJ mixer for my events and even provided setup assistance."</p>
          <div class="testimonial-author">
            <img src="https://via.placeholder.com/60x60" alt="Customer" class="author-img" />
            <div class="author-info">
              <h4>Sarah Williams</h4>
              <p>Event DJ</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="cta-section">
      <div class="cta-content">
        <h2>Ready to Elevate Your Audio Experience?</h2>
        <p>Explore our collection of premium audio equipment and find the perfect solution for your needs.</p>
        <router-link to="/speaker"><button class="cta-button">Shop Now</button></router-link>
      </div>
    </section>

    <!-- NewsletterPage component replaces old newsletter section -->
    <NewsletterPage />

    <!-- FooterPage component replaces old footer -->
    <FooterPage />
  </div>
</template>


<script>
import NavbarPage from "@/components/NavbarPage.vue";
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";
import FooterPage from "@/components/FooterPage.vue";
import NewsletterPage from "@/components/NewsletterPage.vue";

export default {
  components: {
    NavbarPage,
    LoginForm,
    RegisterForm,
    FooterPage,
    NewsletterPage
  },
  data() {
    return {
      showLogin: false,
      showRegister: false
    };
  },
  methods: {
    openLogin() {
      this.showLogin = true;
      this.showRegister = false;
    },
    openRegister() {
      this.showRegister = true;
      this.showLogin = false;
    }
  },
  mounted() {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';
    document.head.appendChild(link);
  }
};
</script>

<style scoped>

/* .hero-section {
  border: 2px solid red;
}
.hero-section {
  border: 2px solid red;
} */




/* Base Styles & Typography */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Baskerville&display=swap');

.landing-page {
  font-family: 'Poppins', sans-serif;
  background: #f8f9fa;
  color: #333;
  line-height: 1.6;
  overflow-x: hidden;
}

.glitter-logo {
  font-family: 'Baskerville', serif;
  font-weight: 700;
  background: linear-gradient(to right, #0c1b3a 0, #4da6ff 20%, #ff6200 40%, #4da6ff 60%, #0c1b3a 80%);
  background-size: 200% auto;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shine 3s linear infinite;
  position: relative;
  display: inline-block;
}
.glitter-logo::before {
  content: "UniTech";
  position: absolute;
  left: 0;
  top: 0;
  z-index: -1;
  color: transparent;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 10px rgba(77, 166, 255, 0.7), 0 0 20px rgba(77, 166, 255, 0.5), 
               0 0 30px rgba(255, 98, 0, 0.5), 0 0 40px rgba(77, 166, 255, 0.3);
  animation: glow 1.5s ease-in-out infinite alternate;
}
@keyframes shine {
  0% {
    background-position: 0% center;
  }
  100% {
    background-position: 200% center;
  }
}
@keyframes glow {
  from {
    text-shadow: 0 0 10px rgba(77, 166, 255, 0.7), 0 0 20px rgba(77, 166, 255, 0.5), 
                 0 0 30px rgba(255, 98, 0, 0.5), 0 0 40px rgba(77, 166, 255, 0.3);
  }
  to {
    text-shadow: 0 0 15px rgba(77, 166, 255, 0.9), 0 0 25px rgba(77, 166, 255, 0.7), 
                 0 0 35px rgba(255, 98, 0, 0.7), 0 0 45px rgba(77, 166, 255, 0.5);
  }
}

.professional-audio {
  font-family: 'Baskerville', serif;
  font-weight: 600;
  color: #4da6ff;
  position: relative;
  display: inline-block;
  text-shadow: 0 0 5px rgba(77, 166, 255, 0.3);
  transition: all 0.3s ease;
}
.professional-audio:hover {
  text-shadow: 0 0 8px rgba(77, 166, 255, 0.5);
}

.rotating-text {
  display: inline-block;
  min-width: 150px;
  font-family: 'Baskerville', serif;
  font-weight: 600;
  color: #4da6ff;
  position: relative;
  text-shadow: 0 0 5px rgba(77, 166, 255, 0.3);
}
.rotating-text::after {
  content: "Audio";
  animation: textRotate 10s linear infinite;
}
@keyframes textRotate {
  0%, 20% {
    content: "Speakers";
  }
  25%, 45% {
    content: "Amplifiers";
  }
  50%, 70% {
    content: "DJ Mixers";
  }
  75%, 95% {
    content: "Microphones";
  }
}

.hero-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 80px 5%;
  background: url('@/assets/background.png') center center/cover no-repeat;
  color: white;
  position: relative;
  overflow: hidden;
  margin-top: 0%;
  margin-bottom: 0%;

}
.hero-content {
  max-width: 600px;
  z-index: 1;
}
.hero-content h1 {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 20px;
}
.hero-content p {
  font-size: 1.1rem;
  margin-bottom: 30px;
  opacity: 0.9;
  color: #f8f9fa;
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

/* Responsive Design */
@media (max-width: 768px) {
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
}
</style>
