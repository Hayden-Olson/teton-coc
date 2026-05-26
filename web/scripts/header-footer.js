// This sets today's date in the header
let now = new Date()
let fulldate = new Intl.DateTimeFormat("en-US", { dateStyle: "medium", timeStyle: "short" }).format(  );
if (navigator.userAgent.toLowerCase().indexOf('firefox') != -1){
    fulldate = new Intl.DateTimeFormat("en-US", { dateStyle: "long", timeStyle: "long" }).format( now );       
}

document.querySelector(".header-today p").textContent = fulldate;

// Toggle the menu open or closed
function toggleMenu(){
    if (navigator.userAgent.toLowerCase().indexOf('firefox') != -1){    
        document.querySelector("nav ul").classList.toggle("menu-active");
        document.querySelector("#hamburger-x").classList.toggle("menu-active");
        document.querySelector("#hamburger-equiv").classList.toggle("menu-active");
    }
}

// Attach click listener to the hamburger menu
document.querySelector("#hamburger-menu").addEventListener('click', toggleMenu);    
