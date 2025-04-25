const { defineConfig } = require('@vue/cli-service');
const webpack = require('webpack');

module.exports = defineConfig({
  transpileDependencies: true,
  productionSourceMap: false,
  devServer: {
    // allowedHosts: 'all', // <-- Add this line
    // hot: false,           // Disable hot module replacement
    // liveReload: false,    // Disable live reload
    // webSocketServer: false, // <--- And this (optional, disables WS server)
  },
  configureWebpack: {
    performance: {
      hints: false,
    },
    plugins: [
      new webpack.DefinePlugin({
        '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': JSON.stringify(false),
      }),
    ],
  },
});
