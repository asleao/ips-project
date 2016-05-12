angular.module("ipsProject").service("usuarioAPI",function($http, config){   

    this.postCadastrarUsuario = function(usuario){
        return $http.post(config.baseUrl +"/pessoas/?format=json",usuario);
    };         
    this.postLogin = function(username,password){       
        return $http.post(config.baseUrl +"/api-auth/login/?next=/backend/pessoas/",{username: username, password:password});
    };   
});