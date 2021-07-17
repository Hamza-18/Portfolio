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

    const skillHeader = document.querySelectorAll(".skill_content")
    skillHeader.forEach(header => header.addEventListener('click',() => {
        header.classList.contains("skill_open")?header.classList.replace("skill_open","skill_close"):
            header.classList.replace("skill_close","skill_open")
    }))
});

function changeSkillListAppearance(header){

}