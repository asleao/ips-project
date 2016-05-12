angular.module("ipsProject").config(function($routeProvider){
        $routeProvider.when("/cadastro",{
            templateUrl:"view/cadastro.html" ,
            controller: "usuarioCtrl"                                   
        });

         $routeProvider.when("/login",{
            templateUrl:"view/login.html" ,
            controller: "usuarioCtrl"                        
        });
        $routeProvider.otherwise({redirectTo: "/home"});      
});