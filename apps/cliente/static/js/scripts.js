/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function main() {

    setupHeaderScroll();

}


function setupHeaderScroll() {
    document.querySelectorAll('li.nav-item a.nav-link').forEach(anchor => {
        scrollToElement(anchor);
    });

    const mainBtn = document.querySelector("#main-btn");
    scrollToElement(mainBtn);
}

function scrollToElement(originElement) {
    originElement.addEventListener('click', function (e) {
        e.preventDefault();
        const targetElement = document.querySelector(this.getAttribute('href'));
        if (!targetElement) return;

        const offset = targetElement.offsetTop - document.querySelector('header').offsetHeight;

        window.scrollTo({
            top: offset,
            behavior: 'smooth'
        });
    })
}
window.onload = main;







