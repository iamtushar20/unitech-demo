<template>
    <div v-if="value" class="spec-item">
      <span class="font-medium">{{ label }}:</span> 
      <span class="text-gray-600">{{ value }}</span>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SpecItem',
    props: {
      label: String,
      value: String
    }
  };
  </script>
  