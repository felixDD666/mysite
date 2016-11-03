
$(document).ready(function() {
    console.log("aqui estamos");
    var f = document.forms["sentMessage"].elements;
    var cansubmit = true;
    $("#id_mensaje").on("keyup",function(){
        for (var i = 1; i < f.length-1; i++) {
            if (f[i].value.length == 0){
                cansubmit = false;
            }
        }
        if (cansubmit) {
            $('#contactSubmit').removeAttr('disabled');
        }
        cansubmit = true;
    });
})


function showThanks(){
    $('#contactSubmitMessage').css("display","block");
}
