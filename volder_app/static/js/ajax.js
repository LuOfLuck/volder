
console.log("holamndo");
$(document).ready(function(){
    $("#sheare").submit(function(e){
        console.log("hola");
        e.preventDefault();
        // $.ajax({
        //     url: $(this).attr('action'),
        //     type: $(this).attr('method'),
        //     data: $(this).serialize(),

        //     success: function(json){
        //         console.log(json);
        //     }

        // })
    })
})