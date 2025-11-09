// script.js — interações simples
document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".nav-links a");
    const current = window.location.pathname;
    navLinks.forEach(link => {
        if (link.href.includes(current)) link.classList.add("active");
    });
});
