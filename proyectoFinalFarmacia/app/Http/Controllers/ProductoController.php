<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Producto;
use App\Http\Helper\ResponseBuilder;
use BD;

class ProductoController extends Controller
{

    public function __construct(){

    }

    public function allSinRestricciones(Request $request)
    {
        $producto = Producto::all();
        $status = true;
        $info = "Producto List";
        return ResponseBuilder::result($status,$info,$producto);
    }

    public function allJson(Request $request){
        if($request->isJson()){
            $producto = Producto::all();
            $status = true;
            $info = "Producto List";
            return ResponseBuilder::result($status,$info,$producto);
            
        }
        $status = false;
        $info = "Unauthorized";
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function getProducto(Request $request, $codigo){
        if ($request->isJson()){
            $producto = Producto::where('codigo', $codigo)->first();
            if(!empty($producto)){
                $status = true;
                $info = "Product is Here";
                return ResponseBuilder::result($status, $info, $producto);
            } else {
                $status = false;
                $info = "Is doesn't here";
                return ResponseBuilder::result($status, $info);
            }
        } else {
            $status = false;
            $info = "Error: Anauthorizade";
            return ResponseBuilder::result($status, $info);
        }
    }

    public function create(Request $request){
        if ($request->isJson()){
            $data = $request->json()->all();
            $producto = Producto::create([
                'codigo' => $data['codigo'],
                'nombre' => $data['nombre'],
                'precio_Unitario' => $data['precio_Unitario'],
                'stock' => $data['stock'],
                'date_created' => $data['date_created']
                
                //"updated_at" => $data['updated_at'],
                //"created_at" => $data['created_at'],
            ]);
            $status = true;
            $info = "Product create succes";
            return ResponseBuilder::result($status, $info, $producto);
        }
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function deleteProducto(Request $request, $codigo){
        if ($request->isJson()){
            $producto = Producto::where('codigo', $codigo)->first();
            if(!empty($producto)){
                
                $producto->delete();
                $status = true;
                $info = "Product is delete";
                return ResponseBuilder::result($status, $info);
            } else {
                $status = false;
                $info = "Is doesn't here";
                return ResponseBuilder::result($status, $info);
            }
        } else {
            $status = false;
            $info = "Error: Anauthorizade";
            return ResponseBuilder::result($status, $info);
        }
    }

}
