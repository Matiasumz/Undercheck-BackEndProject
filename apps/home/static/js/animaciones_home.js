// NAV ACTIVE
const navLinks = document.querySelectorAll('.item');
        const sections = document.querySelectorAll('.secciones');

        function setActiveNavLink() {
        const scrollPosition = document.querySelector('.scroller').scrollTop;

        sections.forEach(section => {
            const top = section.offsetTop - document.querySelector('.scroller').offsetTop;
            const bottom = top + section.offsetHeight;

            if (scrollPosition >= top && scrollPosition < bottom) {
            const sectionId = section.getAttribute('id');
            navLinks.forEach(link => {
                if (link.getAttribute('href') === `#${sectionId}` || link.getAttribute('href') === `/#${sectionId}`) {
                link.classList.add('active');
                } else {
                link.classList.remove('active');
                }
            });
            }
        });
        }

        window.onload = setActiveNavLink;
        document.querySelector('.scroller').addEventListener('scroll', setActiveNavLink);
        
// ANIMAR LISTA
const elementosLi = document.querySelectorAll('#motivos li');

function setActiveLi() {
    const scrollPosition = document.querySelector('.scroller').scrollTop;
    const porQueElegirnosSection = document.getElementById('por-que-elegirnos');

    // Verifica si el scrollPosition está dentro de la sección "Por qué elegirnos"
    if (scrollPosition >= porQueElegirnosSection.offsetTop &&
        scrollPosition < (porQueElegirnosSection.offsetTop + porQueElegirnosSection.offsetHeight)) {
        
        // Aplica la clase con la animación a cada elemento li
        elementosLi.forEach(function (li, index) {
            // Agrega un retraso progresivo a cada elemento li
            setTimeout(function () {
                li.classList.add('animar-lista');
            }, index * 550); // Ajusta el valor del retraso según tus preferencias
        });

        // Elimina el evento de desplazamiento después de aplicar la animación
        window.removeEventListener('scroll', setActiveLi);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Agrega el evento de desplazamiento una vez
    window.addEventListener('scroll', setActiveLi, { once: true });
});

document.querySelector('.scroller').addEventListener('scroll', setActiveLi);



