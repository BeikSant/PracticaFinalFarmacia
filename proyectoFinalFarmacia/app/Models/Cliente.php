<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Cliente extends Model{
    protected $table = 'modelo_cliente';
    protected $fillable = ['cedula','nombres','apellidos','genero','correo','telefono','direccion','date_created'];

    public $timestamps = false;
    
    protected $primaryKey = 'cliente_id';
    /*protected $hidden = [
        'cliente_id'
    ];*/
}