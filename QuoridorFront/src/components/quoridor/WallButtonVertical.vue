
<template>
  <div class="wall-container">
    <div class="wall"></div>
    <div class="up-joint"></div>
    <div class="down-joint"></div>
    <div class="wall"></div>
  </div>
</template>

<style scoped>
.wall-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 33px;
  margin-right: 33px;
  pointer-events: visibleFill;
  transition: background-color 0.3s ease; /* Smooth background transition */
}

.wall {
  width: 14px; /* Slightly increased size for a modern look */
  height: 28px;
  border: 1px solid #d1d1d6; /* Soft border in line with Apple style */
  background-color: #f5f5f7; /* Soft gray background */
  border-radius: 4px; /* Slight rounding to corners */
  transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease; /* Smooth transitions */
}

.up-joint {
  width: 12px;
  height: 12px;
  background: linear-gradient(135deg, #f0f0f5, #d1d1d6); /* Subtle gradient */
  clip-path: polygon(0% 0%, 100% 0%, 50% 100%);
  border: 1px solid #d1d1d6;
  transition: transform 0.3s ease, background-color 0.3s ease; /* Smooth transitions */
}

.down-joint {
  width: 12px;
  height: 12px;
  background: linear-gradient(135deg, #f0f0f5, #d1d1d6); /* Soft gradient in the opposite direction */
  clip-path: polygon(0% 100%, 100% 100%, 50% 0%);
  border: 1px solid #d1d1d6;
  transition: transform 0.3s ease, background-color 0.3s ease; /* Smooth transitions */
}

/* Hover effects */
.wall-container:hover .wall {
  background-color: #e5e5ea; /* Soft gray when hovered */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow on hover */
  transform: translateY(-4px); /* Subtle hover lift effect */
}

.wall-container:hover .up-joint, .wall-container:hover .down-joint {
  background-color: #e5e5ea; /* Matching color for joints on hover */
  transform: translateY(-4px); /* Subtle hover lift effect */
}
</style>