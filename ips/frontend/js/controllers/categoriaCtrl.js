angular.module("ipsProject").controller("categoriaCtrl", function($scope,categoriasAPI,$location){
        $scope.categorias = [];
        var carregarCategorias = function(){
                categoriasAPI.getCategorias().success(function(data){
                       $scope.categorias =data;
                });    
        }; 

        $scope.cadastrarCategoria = function(categoria){            
            categoriasAPI.postCadastrarCategoria(categoria).success(function(data){
               delete $scope.categoria;
                $scope.formCadastroCategoria.$setPristine();
                $location.path("/categoria");
            }); 
        };
        carregarCategorias();      
});