<template>
  <div id="app">
    <router-view></router-view>  <!-- This ensures your routed components are displayed -->
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0; /* <-- Remove or set to 0 */
}

</style>
