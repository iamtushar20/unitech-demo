<template>
    <div class="product-detail-page">
      <!-- Breadcrumb Navigation -->
      <div class="breadcrumb">
        <router-link to="/landingpage">Home</router-link> > 
        <router-link to="/amplifier">Amplifiers</router-link> > 
        <span>TD Series</span>
      </div>
  
      <!-- Product Header -->
      <div class="product-header">
        <h1>Dual Channel Power Amplifier - TD Series</h1>
        <div class="rating">
          <span class="stars">★★★★★</span>
          <span class="reviews">(24 reviews)</span>
        </div>
      </div>
  
      <!-- Product Gallery and Purchase Section -->
      <div class="product-main">
        <!-- Left: Product Images -->
        <div class="product-gallery">
          <div class="main-image">
            <img :src="currentImage" alt="TD Series Amplifier" />
          </div>
          <div class="thumbnail-row">
            <img 
              v-for="(img, index) in productImages" 
              :key="index" 
              :src="img" 
              @click="currentImage = img"
              :class="{ active: currentImage === img }"
              alt="TD Series Thumbnail" 
            />
          </div>
        </div>
  
        <!-- Right: Product Info and Purchase Options -->
        <div class="product-info">
          <div class="model-selector">
            <h3>Select Model</h3>
            <div class="model-options">
              <div 
                v-for="model in models" 
                :key="model.id"
                :class="['model-option', selectedModel.id === model.id ? 'selected' : '']"
                @click="selectedModel = model"
              >
                <h4>{{ model.name }}</h4>
                <p class="price">₹{{ model.price.toLocaleString() }}</p>
              </div>
            </div>
          </div>
  
          <div class="price-box">
            <div class="current-price">₹{{ selectedModel.price.toLocaleString() }}</div>
            <div class="original-price">₹{{ Math.round(selectedModel.price * 1.15).toLocaleString() }}</div>
            <div class="discount">15% off</div>
          </div>
  
          <div class="availability">
            <span class="in-stock">In Stock</span>
            <span class="delivery">Free delivery available</span>
          </div>
  
          <div class="action-buttons">
            <button class="buy-now">Buy Now</button>
            <button class="add-to-cart">Add to Cart</button>
            <button class="wishlist"><i class="heart-icon">♡</i></button>
          </div>
        </div>
      </div>
  
      <!-- Product Details Tabs -->
      <div class="product-details">
        <div class="tabs">
          <div 
            v-for="tab in tabs" 
            :key="tab.id"
            :class="['tab', activeTab === tab.id ? 'active' : '']"
            @click="activeTab = tab.id"
          >
            {{ tab.name }}
          </div>
        </div>
  
        <!-- Description Tab Content -->
        <div v-if="activeTab === 'description'" class="tab-content">
          <div class="description-content">
            <h2>TD Series - Professional Dual Channel Power Amplifier</h2>
            <div class="feature-list">
              <div v-for="(feature, index) in tdSeriesFeatures" :key="index" class="feature-item">
                <div class="bullet">•</div>
                <div class="feature-text">{{ feature }}</div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Specifications Tab Content -->
        <div v-if="activeTab === 'specifications'" class="tab-content">
          <h2>Technical Specifications</h2>
          <table class="specs-table">
            <tr>
              <th>MODEL</th>
              <th>TD-9000</th>
              <th>TD-12000</th>
            </tr>
            <tr v-for="(spec, key) in specifications" :key="key">
              <td>{{ spec.name }}</td>
              <td>{{ spec.td9000 }}</td>
              <td>{{ spec.td12000 }}</td>
            </tr>
          </table>
        </div>
  
        <!-- Reviews Tab Content -->
        <div v-if="activeTab === 'reviews'" class="tab-content">
          <h2>Customer Reviews</h2>
          <div class="review-summary">
            <div class="average-rating">
              <span class="big-rating">4.8</span>
              <div class="stars">★★★★★</div>
              <span class="total-reviews">Based on 24 reviews</span>
            </div>
            <div class="rating-breakdown">
              <div class="rating-bar">
                <span>5 ★</span>
                <div class="bar"><div class="fill" style="width: 85%"></div></div>
                <span>85%</span>
              </div>
              <div class="rating-bar">
                <span>4 ★</span>
                <div class="bar"><div class="fill" style="width: 10%"></div></div>
                <span>10%</span>
              </div>
              <div class="rating-bar">
                <span>3 ★</span>
                <div class="bar"><div class="fill" style="width: 5%"></div></div>
                <span>5%</span>
              </div>
              <div class="rating-bar">
                <span>2 ★</span>
                <div class="bar"><div class="fill" style="width: 0%"></div></div>
                <span>0%</span>
              </div>
              <div class="rating-bar">
                <span>1 ★</span>
                <div class="bar"><div class="fill" style="width: 0%"></div></div>
                <span>0%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Related Products -->
      <div class="related-products">
        <h2>You might also like</h2>
        <div class="product-carousel">
          <div v-for="(product, index) in relatedProducts" :key="index" class="related-product-card">
            <img :src="product.image" alt="Related Product" />
            <h4>{{ product.name }}</h4>
            <div class="related-price">₹{{ product.price.toLocaleString() }}</div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProductDetailPage',
    data() {
      return {
        currentImage: require('@/assets/img1.jpeg'),
        productImages: [
          require('@/assets/img1.jpeg'),
          require('@/assets/img1.jpeg'),
          require('@/assets/img1.jpeg')
        ],
        selectedModel: {
          id: 'td9000',
          name: 'TD-9000',
          price: 145000
        },
        models: [
          {
            id: 'td9000',
            name: 'TD-9000',
            price: 145000
          },
          {
            id: 'td12000',
            name: 'TD-12000',
            price: 175000
          }
        ],
        activeTab: 'description',
        tabs: [
          { id: 'description', name: 'Description' },
          { id: 'specifications', name: 'Specifications' },
          { id: 'reviews', name: 'Reviews' }
        ],
        tdSeriesFeatures: [
          "TD Amplifier provides extensive protection and diagnostic capabilities.",
          "Standard width 19-inch rack mounting. Housed in rugged, all steel 3u chassis.",
          "TD class circuit gives Hi fidelity sound.",
          "Ideal for Hi-end music programme.",
          "3 way operating mode (Bridge, Parallel, Stereo) through selection switch.",
          "4 front LED Indicators for each channel shows ACTIVE (AC Power On), SIGNAL (Sound Output Level), PROTECTION (Faulty Conditions), CLIP (Excessive Signal Output coming from mixer) for ease of operation.",
          "TD series has been designed to operate under stringent working condition such as wide voltage fluctuation due to gensets/AC mains and high ambient temperatures."
        ],
        specifications: [
          { name: "Rated Power (Stereo)", td9000: "2x5200W@2Ω, 2x3850W@4Ω, 2x2100W@8Ω", td12000: "2x5500W@2Ω, 2x4000W@4Ω, 2x2200W@8Ω" },
          { name: "Rated Power (Bridge)", td9000: "7100W@4Ω, 4800W@8Ω", td12000: "7500W@4Ω, 5000W@8Ω" },
          { name: "Damping Factor", td9000: "3000", td12000: "3000" },
          { name: "Smart Protections", td9000: "DC, Short Circuit, Over Load, Over Heat", td12000: "DC, Short Circuit, Over Load, Over Heat" },
          { name: "Input Sensitivity", td9000: "62dB 8Ω 1kHz", td12000: "62dB 8Ω 1kHz" },
          { name: "Frequency Response", td9000: "20Hz-24kHz ±0.1dB", td12000: "20Hz-24kHz ±0.1dB" },
          { name: "Output Circuitry", td9000: "Class TD", td12000: "Class TD" },
          { name: "Input Impedance", td9000: "20kΩ", td12000: "20kΩ" },
          { name: "Input Sensitivity", td9000: "0.75V/1.0V/1.4V", td12000: "0.75V/1.0V/1.4V" },
          { name: "Rack Space", td9000: "3U", td12000: "3U" },
          { name: "S/N Ratio", td9000: "109 dB", td12000: "109 dB" },
          { name: "THD %", td9000: "0.05%@8Ω", td12000: "0.05%@8Ω" },
          { name: "Product Dimensions (mm)", td9000: "480 x 490 x 133", td12000: "480 x 490 x 133" },
          { name: "Weight", td9000: "45Kg", td12000: "48Kg" }
        ],
        relatedProducts: [
          { name: "CA-12+ Amplifier", price: 95000, image: require('@/assets/img1.jpeg') },
          { name: "M-4200 Amplifier", price: 85000, image: require('@/assets/img1.jpeg') },
          { name: "MT-6000 Amplifier", price: 110000, image: require('@/assets/img1.jpeg') },
          { name: "XLi-3600 Amplifier", price: 65000, image: require('@/assets/img1.jpeg') }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .product-detail-page {
    font-family: "Poppins", sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    color: #333;
  }
  
  .breadcrumb {
    margin-bottom: 20px;
    font-size: 14px;
  }
  
  .breadcrumb a {
    color: #4da6ff;
    text-decoration: none;
  }
  
  .breadcrumb a:hover {
    text-decoration: underline;
  }
  
  .product-header {
    margin-bottom: 20px;
  }
  
  .product-header h1 {
    font-size: 28px;
    margin-bottom: 8px;
  }
  
  .rating {
    display: flex;
    align-items: center;
  }
  
  .stars {
    color: #ff9900;
    margin-right: 8px;
  }
  
  .reviews {
    color: #4da6ff;
    cursor: pointer;
  }
  
  .product-main {
    display: flex;
    gap: 40px;
    margin-bottom: 40px;
  }
  
  .product-gallery {
    flex: 1;
  }
  
  .main-image {
    margin-bottom: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .main-image img {
    width: 100%;
    height: auto;
    display: block;
  }
  
  .thumbnail-row {
    display: flex;
    gap: 10px;
  }
  
  .thumbnail-row img {
    width: 60px;
    height: 60px;
    object-fit: cover;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .thumbnail-row img.active {
    border-color: #4da6ff;
  }
  
  .product-info {
    flex: 1;
  }
  
  .model-selector {
    margin-bottom: 20px;
  }
  
  .model-options {
    display: flex;
    gap: 15px;
    margin-top: 10px;
  }
  
  .model-option {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px;
    cursor: pointer;
    transition: all 0.3s ease;
    min-width: 120px;
  }
  
  .model-option:hover {
    border-color: #4da6ff;
  }
  
  .model-option.selected {
    border-color: #4da6ff;
    background-color: rgba(77, 166, 255, 0.05);
  }
  
  .model-option h4 {
    margin: 0 0 8px 0;
  }
  
  .price-box {
    display: flex;
    align-items: baseline;
    margin-bottom: 20px;
  }
  
  .current-price {
    font-size: 28px;
    font-weight: bold;
    margin-right: 10px;
  }
  
  .original-price {
    font-size: 18px;
    color: #999;
    text-decoration: line-through;
    margin-right: 10px;
  }
  
  .discount {
    font-size: 16px;
    color: #00a650;
    font-weight: bold;
  }
  
  .availability {
    margin-bottom: 20px;
  }
  
  .in-stock {
    color: #00a650;
    font-weight: bold;
    margin-right: 15px;
  }
  
  .action-buttons {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;
  }
  
  .buy-now, .add-to-cart {
    padding: 12px 24px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .buy-now {
    background: #ff9900;
    color: white;
  }
  
  .buy-now:hover {
    background: #e68a00;
  }
  
  .add-to-cart {
    background: #4da6ff;
    color: white;
  }
  
  .add-to-cart:hover {
    background: #3a8cd6;
  }
  
  .wishlist {
    width: 46px;
    height: 46px;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    background: white;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .wishlist:hover {
    border-color: #ff6b6b;
    color: #ff6b6b;
  }
  
  .product-details {
    margin-bottom: 40px;
  }
  
  .tabs {
    display: flex;
    border-bottom: 1px solid #e0e0e0;
    margin-bottom: 20px;
  }
  
  .tab {
    padding: 12px 24px;
    cursor: pointer;
    font-weight: 600;
    color: #666;
    border-bottom: 3px solid transparent;
  }
  
  .tab:hover {
    color: #4da6ff;
  }
  
  .tab.active {
    color: #4da6ff;
    border-bottom-color: #4da6ff;
  }
  
  .tab-content {
    padding: 20px 0;
  }
  
  .feature-list {
    margin-top: 20px;
  }
  
  .feature-item {
    display: flex;
    margin-bottom: 12px;
  }
  
  .bullet {
    margin-right: 10px;
    color: #4da6ff;
    font-weight: bold;
  }
  
  .specs-table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .specs-table th, .specs-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .specs-table th {
    background-color: #f5f5f5;
    font-weight: 600;
  }
  
  .review-summary {
    display: flex;
    gap: 40px;
    margin-bottom: 30px;
  }
  
  .average-rating {
    text-align: center;
  }
  
  .big-rating {
    font-size: 48px;
    font-weight: bold;
    line-height: 1;
  }
  
  .total-reviews {
    display: block;
    margin-top: 5px;
    color: #666;
  }
  
  .rating-breakdown {
    flex: 1;
  }
  
  .rating-bar {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
  }
  
  .rating-bar span {
    width: 40px;
  }
  
  .bar {
    flex: 1;
    height: 10px;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin: 0 10px;
  }
  
  .fill {
    height: 100%;
    background-color: #ff9900;
    border-radius: 5px;
  }
  
  .related-products {
    margin-top: 40px;
  }
  
  .product-carousel {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    padding: 10px 0;
  }
  
  .related-product-card {
    min-width: 200px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px;
  }
</style>
  