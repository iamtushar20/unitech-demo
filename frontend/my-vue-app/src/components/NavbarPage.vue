<template>
  <nav class="navbar">
    <div class="logo-container">
      <img src="@/assets/logo.png" alt="UniTech Professional Audio" class="logo" />
    </div>

    <!-- Desktop Nav Links -->
    <ul class="nav-links" v-if="!isMobileMenuOpen">
      <li>
        <router-link
          :to="isLoggedIn ? '/user' : '/'"
          class="nav-link"
          exact
        >Home</router-link>
      </li>
      <li><router-link to="/speaker" class="nav-link" exact>Speakers</router-link></li>
      <li><router-link to="/amplifier" class="nav-link" exact>Amplifiers</router-link></li>
      <li><router-link to="/microphone" class="nav-link" exact>Microphones</router-link></li>
      <li><router-link to="/djmixer" class="nav-link" exact>DJ Mixers</router-link></li>
      <template v-if="isLoggedIn">
        <li>
          <button @click="handleLogout" class="nav-link logout-btn">Logout</button>
        </li>
      </template>
      <template v-else>
        <li>
          <button class="auth-btn" @click="openLogin">Login</button>
        </li>
        <li>
          <button class="auth-btn" @click="openRegister">Signup</button>
        </li>
      </template>
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
            <router-link
              :to="isLoggedIn ? '/user' : '/'"
              class="nav-link"
              exact
              @click="closeMobileMenu"
            >Home</router-link>
          </li>
          <li><router-link to="/speaker" class="nav-link" exact @click="closeMobileMenu">Speakers</router-link></li>
          <li><router-link to="/amplifier" class="nav-link" exact @click="closeMobileMenu">Amplifiers</router-link></li>
          <li><router-link to="/microphone" class="nav-link" exact @click="closeMobileMenu">Microphones</router-link></li>
          <li><router-link to="/djmixer" class="nav-link" exact @click="closeMobileMenu">DJ Mixers</router-link></li>
          <template v-if="isLoggedIn">
            <li>
              <button @click="handleLogout" class="nav-link logout-btn">Logout</button>
            </li>
          </template>
          <template v-else>
            <li>
              <button class="auth-btn" @click="mobileLogin">Login</button>
            </li>
            <li>
              <button class="auth-btn" @click="mobileRegister">Signup</button>
            </li>
          </template>
        </ul>
      </div>
    </transition>

    <!-- Login & Register Modals -->
    <LoginForm
      v-if="showLogin"
      @close="showLogin = false"
      @switch-to-register="openRegister"
      @login-success="onLoginSuccess"
    />
    <RegisterForm
      v-if="showRegister"
      @close="showRegister = false"
      @switch-to-login="openLogin"
      @register-success="onRegisterSuccess"
    />
  </nav>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";
import RegisterForm from "@/components/RegisterForm.vue";

export default {
  name: "NavbarPage",
  components: {
    LoginForm,
    RegisterForm,
  },
  data() {
    return {
      isMobileMenuOpen: false,
      showLogin: false,
      showRegister: false,
      isLoggedInState: !!localStorage.getItem("authToken"),
    };
  },
  computed: {
    isLoggedIn() {
      return this.isLoggedInState;
    },
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
    openLogin() {
      this.showLogin = true;
      this.showRegister = false;
    },
    openRegister() {
      this.showRegister = true;
      this.showLogin = false;
    },
    mobileLogin() {
      this.closeMobileMenu();
      this.$nextTick(() => {
        this.openLogin();
      });
    },
    mobileRegister() {
      this.closeMobileMenu();
      this.$nextTick(() => {
        this.openRegister();
      });
    },
    handleLogout() {
      localStorage.clear();
      this.isLoggedInState = false;
      this.closeMobileMenu();
      this.$router.push("/");
    },
    onLoginSuccess() {
      this.showLogin = false;
      this.isLoggedInState = true;
    },
    onRegisterSuccess() {
      this.showRegister = false;
      this.isLoggedInState = true;
    },
    syncLoginState() {
      this.isLoggedInState = !!localStorage.getItem("authToken");
    },
  },
  mounted() {
    window.addEventListener("storage", this.syncLoginState);
  },
  beforeUnmount() {
    document.body.style.overflow = "";
    window.removeEventListener("storage", this.syncLoginState);
  },
  watch: {
    isLoggedInState(newVal) {
      if (!newVal) {
        this.showLogin = false;
        this.showRegister = false;
      }
    },
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

/* RED LOGOUT BUTTON (desktop) */
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

/* RED LOGOUT BUTTON (mobile) */
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
  margin-left: 10px;
}
.auth-btn:hover {
  background: #1a85ff;
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

/* MODAL OVERLAY FOR LOGIN/REGISTER */
.modal-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3000;
}
.modal-content {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.28);
  padding: 36px 32px 28px 32px;
  max-width: 95vw;
  min-width: 320px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}
:deep(.mobile-nav .logout-btn) {
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

:deep(.mobile-nav .logout-btn:hover) {
  background: #d90429;
  color: #fff;
}

</style>
