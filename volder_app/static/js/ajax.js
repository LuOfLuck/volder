
console.log("holamndo")
$(document).ready(function(){
    $("#sheare").submit(function(e){
        console.log("hola");
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(json, data){
                let perfil = document.getElementById("perfil");
                // perfil.innerHTML += ;
                perfil.innerHTML = "";
                json.forEach((element, i) => {
                    console.log(element)
                    perfil.innerHTML += element.nombre;
                });
            }

        })
    })
})