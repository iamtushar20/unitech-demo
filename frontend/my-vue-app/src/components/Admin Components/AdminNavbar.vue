<template>
    <nav class="navbar">
      <div class="logo-container">
        <img src="@/assets/logo.png" alt="UniTech Admin" class="logo" />
      </div>
  
      <!-- Desktop Nav Links -->
      <ul class="nav-links" v-if="!isMobileMenuOpen">
        <li>
          <router-link to="/admin" class="nav-link" exact>Home</router-link>
        </li>
        <li>
          <router-link to="/admin/add-speaker" class="nav-link" exact>Add Speaker</router-link>
        </li>
        <li>
          <!-- <router-link to="/admin/add-amplifier" class="nav-link" exact>Add Amplifier</router-link> -->
        </li>
        <li>
          <router-link to="/admin/amplifierslist" class="nav-link" exact>Amplifier List</router-link>
        </li>
        <li>
          <router-link to="/admin/speakerslist" class="nav-link" exact>Speaker List</router-link>
        </li>
        <li>
          <button @click="handleLogout" class="nav-link logout-btn">Logout</button>
        </li>
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
            <li>
              <router-link to="/admin" class="nav-link" exact @click="closeMobileMenu">Home</router-link>
            </li>
            <li>
              <router-link to="/admin/add-speaker" class="nav-link" exact @click="closeMobileMenu">Add Speaker</router-link>
            </li>
            <li>
              <!-- <router-link to="/admin/add-amplifier" class="nav-link" exact @click="closeMobileMenu">Add Amplifier</router-link> -->
            </li>
            <li>
              <router-link to="/admin/amplifierslist" class="nav-link" exact @click="closeMobileMenu">Amplifier List</router-link>
            </li>
            <li>
              <router-link to="/admin/speakerslist" class="nav-link" exact @click="closeMobileMenu">Speaker List</router-link>
            </li>
            <li>
              <button @click="handleLogout" class="nav-link logout-btn">Logout</button>
            </li>
          </ul>
        </div>
      </transition>
    </nav>
  </template>
  
  <script>
  export default {
    name: "AdminNavbar",
    data() {
      return {
        isMobileMenuOpen: false,
      };
    },
    methods: {
      toggleMobileMenu() {
        this.isMobileMenuOpen = !this.isMobileMenuOpen;
        document.body.style.overflow = this.isMobileMenuOpen ? "hidden" : "";
      },
      closeMobileMenu() {
        this.isMobileMenuOpen = false;
        document.body.style.overflow = "";
      },
      handleLogout() {
        localStorage.clear();
        this.closeMobileMenu();
        this.$router.push("/");
      },
    },
    beforeUnmount() {
      document.body.style.overflow = "";
    },
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 32px 5%;
    background: rgba(5, 19, 44, 0.9);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
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
  .nav-link.router-link-exact-active {
    color: #4da6ff;
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
  .nav-link.router-link-exact-active::after,
  .nav-link:hover::after {
    width: 100%;
  }
  
  .logout-btn {
    background: #ff3b3b;
    border: none;
    color: #fff;
    cursor: pointer;
    font-size: 25px;
    font-weight: 500;
    padding: 10px 28px;
    border-radius: 30px;
    transition: background 0.2s, color 0.2s;
    margin-left: 10px;
  }
  .logout-btn:hover {
    background: #d90429;
    color: #fff;
  }
  
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
  .mobile-nav .nav-link.router-link-exact-active {
    color: #4da6ff;
  }
  .mobile-nav .logout-btn {
    background: #ff3b3b;
    color: #fff;
    border: none;
    border-radius: 30px;
    padding: 10px 28px;
    font-size: 1.3rem;
    font-weight: 700;
    width: 100%;
    margin: 0 auto;
    display: block;
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
  }
  .mobile-nav .logout-btn:hover {
    background: #d90429;
    color: #fff;
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
  
  @media (max-width: 900px) {
    .nav-links { display: none; }
    .mobile-menu-btn { display: flex; }
  }
  </style>
  