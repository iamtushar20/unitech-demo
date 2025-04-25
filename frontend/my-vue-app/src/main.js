import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router
import VueFeather from 'vue-feather'

const app = createApp(App);

app.use(router); // Use the router
app.component(VueFeather.name, VueFeather)
app.mount('#app');
