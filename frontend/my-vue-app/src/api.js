// // src/api.js
// import axios from 'axios';

// // Use the environment variable for the base URL
// const api = axios.create({
//   baseURL: process.env.VUE_APP_API_URL,
//   // You can add headers or interceptors here if needed
// });

// export default api;


// Modify your src/api.js file
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

// Attach token from localStorage to every request
api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken'); // ✅ FIXED key
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
