
    var app = angular.module('app',[]);


    var func3 = function ($scope) {
        //// jQuery para el scroll suave del menu
        $('a.page-scroll').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: ($($anchor.attr('href')).offset().top - 50)
            }, 1250, 'easeInOutExpo');
            event.preventDefault();
        });

        $('.navbar-collapse ul li a').click(function(){ 
                $('.navbar-toggle:visible').click();
        });
        
        //Para colapsar el menu principal
        $(document).on("scroll", function(){
            var elem = $("#mainNav");
            var pos = elem.offset();
            if(pos.top == 0){
                elem.attr('class' , 'navbar navbar-default navbar-custom navbar-fixed-top affix-top');
                elem.css("opacity", "0.8");
            }else{
                elem.attr('class' , 'navbar navbar-default navbar-custom navbar-fixed-top affix');
                elem.css("opacity", "1");
            }
        });
    }
    app.controller("Controlador2", func3);

/*

    var contactMessage= function ($scope) {
        console.log("aqui estamos")
        var f = document.forms["sentMessage"].elements;
        var cansubmit = true;
        $("#id_mensaje").on("keyup",function(){
            if (cansubmit) {
                $('#contactSubmit').removeAttr('disabled');
            }
        });
        $("#id_mensaje").on("keyup",function(){
            for (var i = 0; i < f.length; i++) {
                console.log(f[i]);
                if (f[i].value.length == 0) cansubmit = false;
            }
            if (cansubmit) {
                $('#contactSubmit').removeAttr('disabled');
            }
        });
        $('#contactSubmit').click(function(){ 
            $('#contactSubmitMessage').css("display","block");
        });
    }

    app.controller("Controlador", contactMessage);

*/


/*
    var formFunc= function ($scope) {
        $scope.formData = {};

        $scope.submitForm = function (formData) {
            alert('Form submitted with' + JSON.stringify(formData));
            
        };
    }

    app.controller("Controlador3" ,  formFunc);


*/