document.getElementById('abrir-popou').addEventListener("click", function(){
    document.querySelector(".cont-popou").style.display = "flex";
    document.getElementById("body").style.overflow ="hidden";
});
document.querySelector('.cerrar-poput').addEventListener("click", function(){
    document.querySelector(".cont-popou").style.display = "none";
    document.getElementById("body").style.overflow ="auto";
});
document.querySelector('.label-url').addEventListener("click", function(){
    inputUrl = document.querySelector(".input-url");
    
    if (inputUrl.style.display != "block"){
        inputUrl.style.display = "block";
    }else{
        inputUrl.style.display = "none";
    }
});
const $seleccionArchivos = document.querySelector("#input-imagen"),
$imagenPrevisualizacion = document.querySelector("#input-imagen-zone");

$seleccionArchivos.addEventListener("change", () => {
const archivos = $seleccionArchivos.files;
if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    $imagenPrevisualizacion.style.display= "none";
    return;
}
const primerArchivo = archivos[0];
const objectURL = URL.createObjectURL(primerArchivo); 
$imagenPrevisualizacion.src = objectURL;
$imagenPrevisualizacion.style.display= "block";
});

contenedorSecretario = document.getElementById("contenedor-secretario");
contenedorPreceptor = document.getElementById("contenedor-preceptor");
contenedorProfesor = document.getElementById("contenedor-profesor");
botonSecretario = document.getElementById("boton-secretario");
botonProfesor = document.getElementById("boton-profesor");
botonPreceptor = document.getElementById("boton-preceptor");
estiloCLick = `
    background-color: rgba(89, 89, 182, 0.795);
    box-shadow: 0 3px rgba(68, 68, 184, 0.795);;
    border: none;
    transform: translateY(4px);
    color: white;
    
`
function mostrarSecretario(){
    contenedorSecretario.style.display = "block";
    botonSecretario.style = estiloCLick;
}
function mostrarProfesor(){
    contenedorProfesor.style.display = "block";
    botonProfesor.style= estiloCLick;
}
function mostrarPreceptor(){
    contenedorPreceptor.style.display = "block";
    botonPreceptor.style= estiloCLick;
}

function ocultar(){
    contenedorSecretario.style.display = "none";
    contenedorPreceptor.style.display = "none";
    contenedorProfesor.style.display = "none";
    botonProfesor.style -= estiloCLick;
    botonPreceptor.style -= estiloCLick;
    botonSecretario.style -= estiloCLick;
}