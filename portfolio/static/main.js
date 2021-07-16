document.addEventListener("DOMContentLoaded", () => {
    /* Hide and show menu*/
    const navMenu = document.getElementById("nav-menu"),
        navToggle = document.getElementById("nav-toggle"),
        navClose = document.getElementById("nav-close");

    const showMenu = () => navMenu.classList.add("show_menu")
    const hideMenu = () => navMenu.classList.remove("show_menu")

    navToggle.onclick = showMenu
    navClose.onclick = hideMenu

    const navIcon = document.querySelectorAll(".nav_item")
    navIcon.forEach(icon => icon.onclick = () => hideMenu())
});