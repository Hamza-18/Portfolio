 document.addEventListener("DOMContentLoaded",() =>{
     const navMenu = document.getElementById("nav-menu"),
         navToggle = document.getElementById("nav-toggle"),
         navClose = document.getElementById("nav-close");
     navToggle.onclick = () => navMenu.classList.add("show_menu")
     navClose.onclick = () =>navMenu.classList.remove("show_menu")
 });