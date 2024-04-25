/*!
* Start Bootstrap - Landing Page v6.0.4 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function generaQR() {
    const div = document.querySelectorAll(".ticket-container");
console.log(div.length);
for(let i = 0; i< div.length; i++)
{
    console.log(div[i].innerHTML);
    let hash = document.querySelectorAll(".hash-container")[i];
    //console.log(hash.innerHTML);
    var qr = new QRCode(div[i], {
        text: hash.innerHTML,
       
    });
}
}
console.log("hola")
generaQR();