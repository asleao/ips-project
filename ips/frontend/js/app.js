angular.module("ipsProject",["ngMessages","ngRoute"]);
angular.module("ipsProject").config(function($httpProvider){      
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';         
});