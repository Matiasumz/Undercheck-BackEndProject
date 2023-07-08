/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function main() {

    setupHeaderScroll();

    let data = await getDjangoData('/get-data/');
    switch (window.location.pathname) {
        case '/':
        case '/clientes/inicio':
            await main_home_client(data.urls);
            break;
        default:
            console.error("Ruta no especificada");
            break;
    }
}

async function main_home_client(urls) {
    const btnIngresar = document.querySelector("#btn-upper");
    const btnCreaEvento = document.querySelector("#btn-bottom");

    btnIngresar.addEventListener("click", () => {
        window.location.pathname = urls[0];
    });
    btnCreaEvento.addEventListener("click", () => {
        window.location.pathname = urls[1];
    });
}

async function getDjangoData(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error("HTTP error " + response.status);
    }
    const data = await response.json();
    return data;
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







