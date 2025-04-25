<template>
    <footer class="site-footer">
      <div class="footer-content">
        <div class="footer-column">
          <h3>UniTech Audio</h3>
          <p>Premium audio solutions for professionals and enthusiasts. Quality sound that transforms experiences.</p>
          <div class="social-icons">
            <a href="https://www.facebook.com/share/14ZehU5jAB/" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
            <a href="https://www.instagram.com/unitech_professional_audio_?igsh=YTlxdWdoaXMxZXQ=&utm_source=ig_contact_invite" class="social-icon"><i class="fab fa-instagram"></i></a>
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
            <li><i class="fas fa-map-marker-alt"></i>17/90 Angoori Bagh Road, Near Red Fort, Delhi - 110006</li>
            <li><i class="fas fa-phone"></i> +91 98776 25472</li>
            <li><i class="fas fa-envelope"></i> unitechprofessionalaudio@gmail.com</li>
          </ul>
          
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
  </template>
  
  <script>
  export default { name: "FooterPage" };
  </script>
  
  <style scoped>
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
  @media (max-width: 768px) {
    .footer-content { grid-template-columns: 1fr; }
    .footer-bottom { flex-direction: column; text-align: center; }
    .footer-bottom-links { margin-top: 20px; }
    .footer-bottom-links a { margin: 0 10px; }
  }
  </style>
  