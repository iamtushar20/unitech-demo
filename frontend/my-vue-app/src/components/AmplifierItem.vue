<template>
  <div class="amplifier-card">
    <img :src="image" alt="Amplifier" class="amplifier-image" />
    <div class="amplifier-info">
      <h3 class="series-name">{{ series }}</h3>
      <p class="description">{{ description }}</p>
      <div class="models">
        <span class="model-label">Models:</span>
        <span v-for="(model, idx) in modelSpecs" :key="model.name" class="model-block">
          <strong>{{ model.name }}</strong>
          <ul class="spec-list">
            <li v-if="model.output4ohmStereo"><strong>Output 4Ω Stereo:</strong> {{ model.output4ohmStereo }}</li>
            <li v-if="model.output8ohmStereo"><strong>Output 8Ω Stereo:</strong> {{ model.output8ohmStereo }}</li>
            <li v-if="model.ratedPowerStereo"><strong>Rated Power (Stereo):</strong> {{ model.ratedPowerStereo }}</li>
            <li v-if="model.output4ohmBridge"><strong>Output 4Ω Bridge:</strong> {{ model.output4ohmBridge }}</li>
            <li v-if="model.output8ohmBridge"><strong>Output 8Ω Bridge:</strong> {{ model.output8ohmBridge }}</li>
            <li v-if="model.ratedPowerBridge"><strong>Rated Power (Bridge):</strong> {{ model.ratedPowerBridge }}</li>
            <li v-if="model.slewRate"><strong>Slew Rate:</strong> {{ model.slewRate }}</li>
            <li v-if="model.dampingFactor"><strong>Damping Factor:</strong> {{ model.dampingFactor }}</li>
            <li v-if="model.fuse"><strong>Fuse:</strong> {{ model.fuse }}</li>
            <li v-if="model.powerSupply"><strong>Power Supply:</strong> {{ model.powerSupply }}</li>
            <li v-if="model.technical"><strong>Technical:</strong> {{ model.technical }}</li>
            <li v-if="model.inputSensitivity"><strong>Input Sensitivity:</strong> {{ model.inputSensitivity }}</li>
            <li v-if="model.inputConnectors"><strong>Input Connectors:</strong> {{ model.inputConnectors }}</li>
            <li v-if="model.inputImpedance"><strong>Input Impedance:</strong> {{ model.inputImpedance }}</li>
            <li v-if="model.inputCMR"><strong>Input CMRR:</strong> {{ model.inputCMR }}</li>
            <li v-if="model.frequencyResponse"><strong>Frequency Response:</strong> {{ model.frequencyResponse }}</li>
            <li v-if="model.bandwidth"><strong>Bandwidth:</strong> {{ model.bandwidth }}</li>
            <li v-if="model.snRatio"><strong>S/N Ratio:</strong> {{ model.snRatio }}</li>
            <li v-if="model.thd"><strong>THD+N:</strong> {{ model.thd }}</li>
            <li v-if="model.imd"><strong>IMD:</strong> {{ model.imd }}</li>
            <li v-if="model.crosstalk"><strong>Crosstalk:</strong> {{ model.crosstalk }}</li>
            <li v-if="model.smartProtections"><strong>Protections:</strong> {{ model.smartProtections }}</li>
            <li v-if="model.indicators"><strong>Indicators:</strong> {{ model.indicators }}</li>
            <li v-if="model.cooling"><strong>Cooling:</strong> {{ model.cooling }}</li>
            <li v-if="model.filterType"><strong>Filter Type:</strong> {{ model.filterType }}</li>
            <li v-if="model.stereoMode"><strong>Stereo Mode:</strong> {{ model.stereoMode }}</li>
            <li v-if="model.productDimensions"><strong>Dimensions:</strong> {{ model.productDimensions }}</li>
            <li v-if="model.packagingDimensions"><strong>Packaging Dimensions:</strong> {{ model.packagingDimensions }}</li>
            <li v-if="model.weight"><strong>Weight:</strong> {{ model.weight }}</li>
            <li v-if="model.productGrossWeight"><strong>Gross Weight:</strong> {{ model.productGrossWeight }}</li>
          </ul>
          <span v-if="idx !== modelSpecs.length - 1" class="model-divider"></span>
        </span>
      </div>
      <button class="details-button">View Details</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "AmplifierItem",
  props: {
    series: String,
    description: String,
    image: String,
    // Pass an array of model objects as shown below
    modelSpecs: {
      type: Array,
      required: true,
      default: () => []
    }
  }
};
</script>

<style scoped>
.amplifier-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.amplifier-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 15px;
}

.amplifier-info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.series-name {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #0c1b3a;
}

.description {
  color: #555;
  margin-bottom: 15px;
  flex: 1;
}

.models {
  margin-bottom: 15px;
  font-size: 0.97rem;
}

.model-label {
  font-weight: bold;
  color: #4da6ff;
  margin-right: 6px;
}

.model-block {
  display: block;
  margin-bottom: 10px;
}

.spec-list {
  list-style: none;
  padding: 0;
  margin: 5px 0 0 0;
  font-size: 0.93em;
}
.spec-list li {
  margin-bottom: 2px;
  line-height: 1.2;
}

.model-divider {
  display: block;
  height: 1px;
  background: #e0e7ef;
  margin: 10px 0;
}

.details-button {
  background: #0c1b3a;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
  align-self: flex-start;
}

.details-button:hover {
  background: #4da6ff;
}
</style>
