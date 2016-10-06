
    //funcion para minimo de caracteres;
    var app = angular.module('app',[])


    var func2 = function($scope) {
        console.log("hola2");
            
        $scope.errorMinimo = false;

        $scope.$watch('name', function (nuevo, anterior) {

        if (!nuevo) return;

        if (nuevo.length < 6) {
            $scope.errorMinimo = true;
            } else {
            $scope.errorMinimo = false;
            }
        })
    }

    app.controller("Controlador", func2)

    var func3 = function ($scope) {
        $(document).on("scroll", function(){
            var elem = $("#mainNav");
            var pos = elem.offset();
            if(pos.top == 0){
                elem.attr('class' , 'navbar navbar-default navbar-custom navbar-fixed-top affix-top');
                elem.css("opacity", "0.7");
            }else{
                elem.attr('class' , 'navbar navbar-default navbar-custom navbar-fixed-top affix');
                elem.css("opacity", "1");
            }
        });
    }
    app.controller("Controlador2", func3)


    var formFunc= function ($scope) {
        console.log("holaform");
        $scope.formData = {};

        $scope.submitForm = function (formData) {
            alert('Form submitted with' + JSON.stringify(formData));
        };
    }

    app.controller("Controlador3" ,  formFunc);






