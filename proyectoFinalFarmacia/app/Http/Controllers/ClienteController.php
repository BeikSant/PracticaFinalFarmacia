<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Cliente;
use App\Http\Helper\ResponseBuilder;
use BD;

class ClienteController extends Controller
{

    public function __construct(){

    }

    public function allSinRestricciones(Request $request)
    {
        $cliente = Cliente::all();
        $status = true;
        $info = "Cliente List";
        return ResponseBuilder::result($status,$info,$cliente);
    }

    public function allJson(Request $request){
        if($request->isJson()){
            $cliente = Cliente::all();
            $status = true;
            $info = "Clients List";
            return ResponseBuilder::result($status,$info,$cliente);
            
        }
        $status = false;
        $info = "Unauthorized";
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function getCliente(Request $request, $cedula){
        if ($request->isJson()){
            $cliente = Cliente::where('cedula', $cedula)->first();
            if(!empty($cliente)){
                $status = true;
                $info = "Client is Here";
                return ResponseBuilder::result($status, $info, $cliente);
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
            $cliente = Cliente::create([
                'cedula' => $data['cedula'],
                'nombres' => $data['nombres'],
                'apellidos' => $data['apellidos'],
                'genero' => $data['genero'],
                "correo" => $data['correo'],
                "telefono" => $data['telefono'],
                "direccion" => $data['direccion'],
                "date_created" => $data['date_created'],
                //"updated_at" => $data['updated_at'],
                //"created_at" => $data['created_at'],
            ]);
            $status = true;
            $info = "Client create succes";
            return ResponseBuilder::result($status, $info, $cliente);
        }
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function deleteCliente(Request $request, $cedula){
        if ($request->isJson()){
            $cliente = Cliente::where('cedula', $cedula)->first();
            if(!empty($cliente)){
                
                $cliente->delete();
                $status = true;
                $info = "Client is delete";
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
