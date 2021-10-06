const navToggler = document.querySelectorAll(".nav__toggler");
navToggler.forEach(e => e.addEventListener('click', function () {
    const element = this.parentElement;
    element.classList.toggle("collapsible--expanded");
}));
const disables = document.querySelectorAll(".page-link");
disables.forEach(e => {
    if (e.parentElement.classList.contains('disabled'))
        e.setAttribute('tabindex', '-1');
});