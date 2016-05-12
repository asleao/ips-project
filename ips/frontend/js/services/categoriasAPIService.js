angular.module("ipsProject").service("categoriasAPI",function($http, config){
  
   this.getCategorias = function(){
        return $http.get(config.baseUrl + "/categoria/?format=json");
    };

    this.getCategoria = function(id){
        return $http.get(config.baseUrl + "/categoria/"+id+"/?format=json");
    };

     this.postCadastrarCategoria = function(categoria){
        return $http.post(config.baseUrl +"/categoria/?format=json",categoria);
    };   
});