<template>
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
  </template>
  
  <script>
  export default { name: "NewsLetter" };
  </script>
  
  <style scoped>
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
  @media (max-width: 768px) {
    .newsletter-form { flex-direction: column; }
  }
  </style>
  