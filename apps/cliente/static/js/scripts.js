/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function main() {

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

window.onload = main;







