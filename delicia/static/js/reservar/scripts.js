document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".reserva-form");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        alert("Reserva enviada com sucesso! Entraremos em contato para confirmar.");
        form.reset();
    });
});
