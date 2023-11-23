const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", ()=> {
     hamburger.classList.toggle("activate");
     navMenu.classList.toggle("activate");
})

document.querySelectorAll(".nav-link").forEach(n=> n.addEventListener("click", ()=>  {
     hamburger.classList.remove("activate");
     navMenu.classList.remove("activate");
}))

window.addEventListener('load', function() {
     var navbar = document.querySelector('.navbar');
     navbar.style.opacity = 1;
   });
   