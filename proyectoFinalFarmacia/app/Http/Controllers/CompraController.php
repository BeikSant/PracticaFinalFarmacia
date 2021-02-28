<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Producto;
use App\Models\Cliente;
use App\Models\Compra;
use App\Http\Helper\ResponseBuilder;
use DB;

class CompraController extends Controller{

    public function __construct(){
        //
    }
    public function comprar(Request $request, $cedula, $codigo){
        if ($request->isJson()){
            $cliente = Cliente::where('cedula', $cedula)->first();
            if(!empty($cliente)){
                $producto = Producto::where('codigo',$codigo)->first();
                if(!empty($producto)){
                    $data = $request->json()->all();
                    if ($data['numero_Productos']<=$producto->stock && $data['numero_Productos']>0){
                        $compra = Compra::create([
                            'fecha' => $data['fecha'],
                            'numero_Productos' => $data['numero_Productos'],
                            'valor_Total' => $data['numero_Productos']*$producto->precio_Unitario,
                            'descripcion' => $data['descripcion'],
                            "product_id" => $producto->producto_id,
                            "cliente_id" => $cliente->cliente_id,
                            "date_created" => $data['date_created'],
                            "updated_ad" => $data['updated_ad'],
                            ]);
                        $producto->stock = $producto->stock-$data['numero_Productos'];
                        $producto->save();
                        $status = true;
                        $info = "Compra exitosa";
                        return ResponseBuilder::result($status, $info, $compra.$producto);
                    } else {
                        $status = false;
                        $info = "Stock Insuficiente";
                        return ResponseBuilder::result($status, $info);
                    } 
                } else {
                    $status = false;
                    $info = "Producto no existente";
                    return ResponseBuilder::result($status, $info);
            }
            } else {
                $status = false;
                $info = "Cliente no existente";
                return ResponseBuilder::result($status, $info);
            }
        } else {
            $status = false;
            $info = "Error: Anauthorizade";
            return ResponseBuilder::result($status, $info);
        }
    }
}