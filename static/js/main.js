// // HERO SLIDER
// new Swiper(".heroSwiper", {
//   loop: true,
//   autoplay: {
//     delay: 5000,
//   },
//   pagination: {
//     el: ".swiper-pagination",
//     clickable: true,
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });

// // TOURS SLIDER
// new Swiper(".tourSwiper", {
//   slidesPerView: 3,
//   spaceBetween: 30,
//   loop: true,
//   autoplay: {
//     delay: 4000,
//   },
//   breakpoints: {
//     0: { slidesPerView: 1 },
//     768: { slidesPerView: 2 },
//     1024: { slidesPerView: 3 },
//   },
// });

// // AOS INIT
// AOS.init({
//   duration: 1000,
//   once: true,
// });

document.addEventListener('DOMContentLoaded', function () {

  // ===== HERO SLIDER =====
  const heroSwiperEl = document.querySelector(".heroSwiper");
  const heroSlides = heroSwiperEl ? heroSwiperEl.querySelectorAll(".swiper-slide") : [];
  const loopEnabled = heroSlides.length > 1; // only loop if more than 1 slide

  new Swiper(".heroSwiper", {
    loop: loopEnabled,
    speed: 1200,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // ===== AOS ANIMATIONS =====
  AOS.init({
    duration: 1000,
    once: true,
  });

  // ===== SMOOTH SCROLL FOR HERO BUTTON =====
  const scrollButton = document.querySelector('.hero-overlay a[href^="#featured-tours"]');
  if (scrollButton) {
    scrollButton.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        window.scrollTo({
          top: targetSection.offsetTop - 80, // adjust for fixed navbar height if needed
          behavior: 'smooth'
        });
      }
    });
  }

  // Navbar scroll effect
const navbar = document.querySelector(".main-navbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});
});
