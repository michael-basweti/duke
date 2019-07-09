const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('message').fadeOut('slow');
}, 3000);

$(document).ready(function() {
  $(".testimonial-carousel").slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: false,
    arrows: true,
    prevArrow: $(".testimonial-carousel-controls .prev"),
    nextArrow: $(".testimonial-carousel-controls .next")
  });
});