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

    /*========navigation=======================*/
    const navLink = document.querySelectorAll(".nav_link")
    navLink.forEach(nav => nav.addEventListener('click', () => navLink.forEach(_nav => _nav !== nav ?
        _nav.classList.remove("nav_active") : _nav.classList.add("nav_active"))))

    /*=========Skills==================*/
    const skillHeader = document.querySelectorAll(".skill_content")
    skillHeader.forEach(header => header.addEventListener('click', () => {
        skillHeader.forEach(_header => header === _header ? openSkill(_header, true) : openSkill(_header, false))
    }))

    function openSkill(header, bool) {
        bool ? header.classList.contains("skill_open") ? header.classList.replace("skill_open", "skill_close") :
            header.classList.replace("skill_close", "skill_open") :
            header.classList.replace("skill_open", "skill_close")
    }

    /*=========Services===============*/
    const serviceBtn = document.querySelectorAll(".services_button"),
        models = document.querySelectorAll(".services_model"),
        modelCloseBtn = document.querySelectorAll(".services_model-close")
    serviceBtn.forEach((btn, i) => btn.addEventListener('click', () => {
        models[i].classList.add("show_model")
    }))
    modelCloseBtn.forEach(btn => btn.addEventListener('click', () => {
        models.forEach(model => model.classList.remove("show_model"))
    }))
    /*============Projects======================*/
    const swiper = new Swiper('.projects_container', {
        cssMode: true,
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
    });

    /*=========Scroll===================*/
    const sections = document.querySelectorAll('section[id]')

    function scrollActive() {
        const scrollY = window.pageYOffset

        sections.forEach(current => {
            const sectionHeight = current.offsetHeight
            const sectionTop = current.offsetTop - 70;
            let sectionId = current.getAttribute('id')
            if (window.scrollY >= 2750) {
                document.querySelectorAll(".nav_menu a").forEach(nav => nav.getAttribute("href")
                === "#contact me" ? nav.classList.add("nav_active") : nav.classList.remove("nav_active"))
            }
            else if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                const menu = document.querySelectorAll(".nav_menu a")
                menu.forEach(nav => nav.getAttribute("href") === "#" + sectionId ? nav.classList.add("nav_active") :
                    nav.classList.remove("nav_active"));
            }
        })
    }

    window.addEventListener('scroll', scrollActive)

});
