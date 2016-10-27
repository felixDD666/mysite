
 

    //funcion para minimo de caracteres;
    var app = angular.module('app',[])


    var func2 = function($scope) {

            
        

            /*
        $('.bg').scroll(function() {
            console.log("hola");
            var x = $(this).scrollTop();
            $(this).css('background-position', '0% ' + parseInt(-x / 10) + 'px');
        });
        */
        
        // Closes the Responsive Menu on Menu Item Click
        

        
            
    }

    app.controller("Controlador", func2)

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
    app.controller("Controlador2", func3)


    var formFunc= function ($scope) {
        $scope.formData = {};

        $scope.submitForm = function (formData) {
            alert('Form submitted with' + JSON.stringify(formData));
            
        };
    }

    app.controller("Controlador3" ,  formFunc);






