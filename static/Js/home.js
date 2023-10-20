document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".slider");
  const prevBtn = document.querySelector(".prev");
  const nextBtn = document.querySelector(".next");

  let currentIndex = 0;

  function showSlide(index) {
    const offset = -index * 100; // Assuming each slide takes 100% width
    slider.style.transform = `translateX(${offset}%)`;
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % 3; // Change 3 to the number of images you have
    showSlide(currentIndex);
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + 3) % 3; // Change 3 to the number of images you have
    showSlide(currentIndex);
  }

  // Event listeners for navigation
  nextBtn.addEventListener("click", nextSlide);
  prevBtn.addEventListener("click", prevSlide);
  const button = document.getElementById("next");

  function simulateButtonClick() {
    button.click();
  }
  const intervalId = setInterval(simulateButtonClick, 5000);
});
