<script setup>
import WallButtonHorizontal from "@/components/quoridor/WallButtonHorizontal.vue";
import WallButtonVertical from "@/components/quoridor/WallButtonVertical.vue";
</script>

<template>
  <div class="containers">
    <h1>This is an Quoridor page</h1>
    <div class="grids">
      <div class="grid">
        <div class="cellgrid">
          <div class="row" v-for="row in 9" :key="row">
            <div class="cell" v-for="cell in 9" :key="cell">
              {{ row }}-{{ cell }}
            </div>
          </div>
        </div>
      </div>
      <div class="grid">
        <div class="wallgrid">
          <div class="row" v-for="row in 8" :key="row">
            <div class="horizontal-wall" v-for="cell in 8" :key="cell">
              <WallButtonHorizontal />
            </div>
          </div>
        </div>
      </div>
      <div class="grid">
        <div class="wallgrid">
          <div class="row" v-for="row in 8" :key="row">
            <div class="horizontal-wall" v-for="cell in 8" :key="cell">
              <WallButtonVertical />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center; /* Centered content */
    background-color: #f5f5f7; /* Light neutral background */
  }
}

.row {
  display: flex;
  justify-content: center;
}

.cell {
  width: 60px; /* Slightly larger cells for a more modern feel */
  height: 60px;
  border: 1px solid #d1d1d6; /* Subtle border with light gray */
  border-radius: 12px; /* Rounded corners for modern design */
  background-color: #ffffff; /* Clean white background */
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
  pointer-events: visibleFill;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transitions */
}

.cell:hover {
  background-color: #e5e5ea; /* Soft gray on hover */
  transform: translateY(-4px); /* Subtle hover lift effect */
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15); /* Deeper shadow on hover */
}

.grid {
  position: absolute;
  pointer-events: none;
  border-radius: 10px; /* Rounded edges for grid */
}

.wallgrid {
  position: relative;
  left: 40px;
  top: 40px;
}

.cellgrid {
  position: relative;
  left: 0px;
  top: 0px;
}
</style>
