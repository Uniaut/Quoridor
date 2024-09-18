
<template>
  <div class="wall-container">
    <div class="wall"></div>
    <div class="left-joint"></div>
    <div class="right-joint"></div>
    <div class="wall"></div>
  </div>
</template>

<style scoped>
.wall-container {
  display: flex;
  align-items: center;
  justify-content: center; /* Center content horizontally */
  margin-top: 31px;
  margin-bottom: 31px;
  pointer-events: visibleFill;
  transition: background-color 0.3s ease; /* Smooth background transition */
}

.wall {
  width: 28px;
  height: 18px; /* Slightly increased height for balance */
  border: 1px solid #d1d1d6; /* Softer border */
  background-color: #f5f5f7; /* Light, neutral background */
  border-radius: 4px; /* Slight rounding for a modern look */
  transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease; /* Smooth transitions */
}

.left-joint {
  width: 12px; /* Match size with other joints */
  height: 12px;
  background: linear-gradient(135deg, #f0f0f5, #d1d1d6); /* Soft gradient */
  clip-path: polygon(0% 100%, 0% 0%, 100% 50%);
  border: 1px solid #d1d1d6;
  transition: transform 0.3s ease, background-color 0.3s ease; /* Smooth transitions */
}

.right-joint {
  width: 12px;
  height: 12px;
  background: linear-gradient(135deg, #f0f0f5, #d1d1d6); /* Soft gradient */
  clip-path: polygon(0% 50%, 100% 100%, 100% 0%);
  border: 1px solid #d1d1d6;
  transition: transform 0.3s ease, background-color 0.3s ease; /* Smooth transitions */
}

/* Hover effects */
.wall-container:hover .wall {
  background-color: #e5e5ea; /* Soft gray when hovered */
  transform: translateY(-4px); /* Subtle hover lift effect */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow for depth */
}

.wall-container:hover .left-joint, .wall-container:hover .right-joint {
  background-color: #e5e5ea; /* Matching hover effect for joints */
  transform: translateY(-4px); /* Subtle hover lift effect */
}
</style>