/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function main() {

    let url = await getDjangoData('/get-data/');
    switch (window.location.pathname) {
        case '/':
            await main_home_client();
            break;
        default:
            console.error("Ruta no especificada");
            break;
    }
}

async function main_home_client() {
    const btnIngresar = document.querySelector("#btn-ingresar");
    const btnCreaEvento = document.querySelector("#btn-crea-evento");
    const data = await getDjangoData('/get-data/');
    btnIngresar.addEventListener("click", () => {
        window.location.pathname = data.login_url;
    });
    btnCreaEvento.addEventListener("click", () => {
        window.location.pathname = data.crear_evento_url;
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

main();







