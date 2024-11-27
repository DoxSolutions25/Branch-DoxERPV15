function initialize() {
$(".form-login").on("submit", () => {
    localStorage.setItem("set_session", 1);
});
}
$(window).ready(initialize)