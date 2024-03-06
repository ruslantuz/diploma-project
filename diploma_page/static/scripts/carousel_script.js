var swiperMob = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 32,
  breakpoints: {
    1120: {
      slidesPerView: 2
    },
    1600: {
      slidesPerView: 3
    },
    2300: {
      slidesPerView: 4
    }
  },
  grabCursor: true,
  navigation: {
    nextEl: ".destinations .arrow-right",
    prevEl: ".destinations .arrow-left",
  },

});

var offerSwiperMob = new Swiper(".offerSwiper", {
  slidesPerView: 1,
  spaceBetween: 32,
  breakpoints: {
    1122: {
      slidesPerView: 3
    }
  },
  grabCursor: false,
  navigation: {
    nextEl: ".special-offers .arrow-right",
    prevEl: ".special-offers .arrow-left",
  },
});

plannerSwiper = new Swiper(".plannerSwiper", {
  slidesPerView: 1,
  spaceBetween: 32,
  breakpoints: {
    1122: {
      slidesPerView: 2.5
    },
    1400: {
      slidesPerView: 3
    }
  },
  grabCursor: true
});
