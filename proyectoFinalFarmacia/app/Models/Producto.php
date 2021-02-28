<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Producto extends Model{
    protected $table = 'modelo_producto';
    protected $fillable = ['codigo','nombre','numero_Productos','stock','precio_Unitario','date_created'];

    public $timestamps = false;

    protected $primaryKey = 'producto_id';
    /*protected $hidden = [
        'cliente_id'
    ];*/
}