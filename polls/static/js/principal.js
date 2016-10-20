
    //funcion para minimo de caracteres;
    var app = angular.module('app',[])


    var func2 = function($scope) {

            // jQuery for page scrolling feature - requires jQuery Easing plugin
        $('a.page-scroll').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: ($($anchor.attr('href')).offset().top - 50)
            }, 1250, 'easeInOutExpo');
            event.preventDefault();
        });

        
        
        // Closes the Responsive Menu on Menu Item Click
        $('.navbar-collapse ul li a').click(function(){ 
                $('.navbar-toggle:visible').click();
        });

        
            
    }

    app.controller("Controlador", func2)

    var func3 = function ($scope) {
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






