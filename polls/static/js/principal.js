
    //funcion para minimo de caracteres;
    var app = angular.module('app',[])

    var func1 = function($scope){
        console.log("hola1");
        var hide = true;
        console.log(hide);
        $scope.func1 = function() {
            hide = false;
            console.log(hide);
        }
    };

    app.controller("Controlador1", func1);

    var func2 = function($scope) {
        console.log("hola2");
            
        $scope.errorMinimo = false;

        $scope.$watch('Name', function (nuevo, anterior) {

        if (!nuevo) return;

        if (nuevo.length < 6) {
            $scope.errorMinimo = true;
            } else {
            $scope.errorMinimo = false;
            }
        })
    }

    app.controller("Controlador2", func2)

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



    // Configuración de las rutas
    /* para cuando necesitemos navegar
    app.config(function($routeProvider) {

        $routeProvider
            .when('/', {
                templateUrl : '../../../templates/polls/pruebaRoute.html',
                controller  : 'Controlador1'
            })
            .when('/principal', {
                templateUrl : '../../../templates/polls/pruebaRoute.html',
                controller  : 'Controlador1'
            })
            
    });

    */





