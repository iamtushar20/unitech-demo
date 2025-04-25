<template>
  <div class="amplifier-card">
    <img :src="amplifier.image_url" :alt="amplifier.model_name" class="amp-image" v-if="amplifier.image_url" />
    <h3 class="product-title">{{ amplifier.model_name }}</h3>
    <ul class="amp-details">
      <li v-for="(detail, index) in topFiveDetails" :key="index">
        <strong>{{ detail.label }}:</strong> {{ detail.value }}
      </li>
    </ul>
    <button class="details-btn" @click="goToDetails">View Details</button>
  </div>
</template>


<script>
export default {
  name: 'AmplifierCard',
  props: {
    amplifier: {
      type: Object,
      required: true,
    },
  },
  computed: {
    topFiveDetails() {
      const fields = [
        { label: 'Power Supply', value: this.amplifier.power_supply },
        { label: 'Rated Power Stereo', value: this.amplifier.rated_power_stereo },
        { label: 'Frequency Response', value: this.amplifier.frequency_response },
        { label: 'Input Impedance', value: this.amplifier.input_impedance },
        { label: 'Damping Factor', value: this.amplifier.damping_factor },
        { label: 'Cooling', value: this.amplifier.cooling },
        { label: 'THD', value: this.amplifier.thd },
        { label: 'Input Connectors', value: this.amplifier.input_connectors },
        { label: 'Rated Power Bridge', value: this.amplifier.rated_power_bridge },
      ];

      // Pull out weight separately
      const weightField = {
        label: 'Weight',
        value: this.amplifier.weight
      };

      // Filter non-empty fields and limit to 5 (excluding weight initially)
      const selected = fields.filter(f => f.value).slice(0, 5);

      // If weight exists and isn’t already in, include it as the last item (by dropping the last one)
      if (weightField.value) {
        if (selected.length === 5) selected.pop();
        selected.push(weightField);
      }

      return selected;
    }
  },
  methods: {
    goToDetails() {
      this.$router.push({ name: 'AmplifierDetails', params: { id: this.amplifier.id } });
    },
  },
};
</script>


<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

/* .amplifier-card {
  background: linear-gradient(to right, #f8fbff, #eef4fc);
  border-radius: 18px;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
  padding: 24px 20px;
  margin: 20px 0;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
} */

.amplifier-card {
  position: relative;
  background: linear-gradient(145deg, #f0f4f8, #e2e8f0); /* soft bluish-gray gradient */
  border-radius: 20px;
  padding: 28px 24px;
  margin: 24px 0;
  text-align: center;
  box-shadow:
    0 10px 25px rgba(0, 0, 0, 0.08),
    inset 0 0 4px rgba(255, 255, 255, 0.4); /* subtle internal glow for soft glassy look */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  backdrop-filter: blur(4px); /* glass feel */
  border: 1px solid rgba(203, 213, 225, 0.6); /* cool border */
  overflow: hidden;
  z-index: 1;
}

.amplifier-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.3) 1px, transparent 0);
  background-size: 18px 18px;
  opacity: 0.05;
  z-index: 0;
  pointer-events: none;
}


.amplifier-card > * {
  position: relative;
  z-index: 1;
}
 
.amplifier-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
}
.amp-image {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  margin-bottom: 20px;
  object-fit: cover;
}
.amp-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 14px;
  color: #003366;
}
.amp-details {
  list-style: none;
  padding: 0;
  margin: 0 0 20px 0;
  text-align: left;
}
.amp-details li {
  font-size: 1rem;
  margin-bottom: 8px;
  color: #444;
}
.details-btn {
  background: #4da6ff;
  color: #fff;
  border: none;
  border-radius: 30px;
  padding: 10px 30px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease-in-out;
}
.details-btn:hover {
  background: #1a85ff;
}


.product-title {
  font-size: 2.8rem;
  font-weight: 800;
  text-align: center;
  line-height: 1.3;
  letter-spacing: -0.5px;
  background: linear-gradient(90deg, #0f172a, #1e40af);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  font-family: 'Orbitron', 'Segoe UI', sans-serif;
  margin-top: 1rem;
  margin-bottom: 1.5rem;
}

.product-title::after {
  content: '';
  display: block;
  width: 120px;
  height: 3px;
  margin: 12px auto 0;
  background: linear-gradient(90deg, #2563eb, #60a5fa);
  border-radius: 3px;
  transition: width 0.3s ease-in-out;
}

.product-title:hover::after {
  width: 160px;
}

.product-title:hover {
  text-shadow: 0 0 10px rgba(96, 165, 250, 0.4), 0 0 20px rgba(96, 165, 250, 0.2);
}


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

.amp-details {
  list-style: none;
  padding: 0;
  margin: 0 0 20px 0;
  text-align: left;
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  line-height: 1.6;
  color: #1e293b;
}

.amp-details li {
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed rgba(0, 0, 0, 0.05);
  padding-bottom: 4px;
}

.amp-details li strong {
  color: #334155;
  font-weight: 600;
  min-width: 160px;
  display: inline-block;
}

.amp-details li span {
  color: #0f172a;
  font-weight: 400;
}


@media (max-width: 768px) {
  .amp-details {
    text-align: center;
    margin: 0 auto;
  }
}


</style>
