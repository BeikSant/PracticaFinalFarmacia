<?php

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router -> group(['prefix' => 'cliente'], function($router){
    $router -> group(['middleware' => 'auth'], function() use ($router){
        
    });
    $router -> post('new','ClienteController@create'); 
    $router -> get('all', 'ClienteController@allSinRestricciones');
    $router -> get('allJson', 'ClienteController@allJson');
    $router -> get('get/{cedula}','ClienteController@getCliente');
    $router -> get('delete/{cedula}','ClienteController@deleteCliente');
}); 


$router -> group(['prefix' => 'producto'], function($router){
    $router -> group(['middleware' => 'auth'], function() use ($router){
        
    });
    $router -> post('new','ProductoController@create'); 
    $router -> get('all', 'ProductoController@allSinRestricciones');
    $router -> get('allJson', 'ProductoController@allJson');
    $router -> get('get/{codigo}','ProductoController@getProducto');
    $router -> get('delete/{codigo}','ProductoController@deleteProducto');
}); 

$router -> group(['prefix' => 'compra'], function($router){
    $router -> group(['middleware' => 'auth'], function() use ($router){
        
    });
    $router -> post('comprar/{cedula}/{codigo}','CompraController@comprar'); 
}); 


$router -> group(['prefix' => 'usuario'], function($router){
    $router -> post('login', 'UserController@login');
    $router -> post('salir', 'UserController@logout');
}); 
