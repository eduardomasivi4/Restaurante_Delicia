// ================= NAVBAR EFEITO SCROLL =================

window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {
        navbar.style.background = "rgba(8, 8, 8, 0.95)";
        navbar.style.padding = "18px 80px";
        navbar.style.transition = "0.3s";
    } else {
        navbar.style.background = "rgba(13, 13, 13, 0.9)";
        navbar.style.padding = "25px 80px";
    }
});


// ================= SCROLL SUAVE =================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});


// ================= ANIMAÇÃO AO SCROLL =================

const sections = document.querySelectorAll("section");

const revealSection = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = "translateY(0px)";
            entry.target.style.transition = "all 1s ease";
            observer.unobserve(entry.target);
        }
    });
};

const sectionObserver = new IntersectionObserver(revealSection, {
    threshold: 0.15
});

sections.forEach(section => {
    section.style.opacity = 0;
    section.style.transform = "translateY(60px)";
    sectionObserver.observe(section);
});


// ================= FEEDBACK RESERVA =================

const form = document.querySelector(".reservation-form");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    alert("Reserva enviada com sucesso! Em breve entraremos em contacto.");

    form.reset();
});