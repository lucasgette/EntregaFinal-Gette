const hamburguesa = document.querySelector('.hamburguesa')
const nav = document.querySelector('.lista-enlaces');

hamburguesa.addEventListener('click', openNav)

function openNav() {
    // Para la pelotudez de la cruz
    console.log('HI')
    hamburguesa.classList.toggle('active'); 

    const nav = document.querySelector('.lista-enlaces');
    nav.classList.toggle("open");

    if(nav.classList.contains("open")) {
        nav.style.maxHeight = nav.scrollHeight + "px"

        if(listaControles.classList.contains('open')) {
            profileControl()
        }
    }

    else {
        nav.removeAttribute("style");
    }
}



const fotoPerfil = document.querySelector('.perfil-logo')

fotoPerfil.addEventListener('click', profileControl)


const listaControles = document.querySelector('.control-usuario');

function profileControl() { 
        
    listaControles.classList.toggle("open");

    if(listaControles.classList.contains("open")) {
        listaControles.style.maxHeight = listaControles.scrollHeight + "px" 
        
        if(nav.classList.contains("open")) {
            console.log('ABIERTOOOOO')
            openNav()
        }
    }

    else {
        listaControles.removeAttribute("style");
    }

}