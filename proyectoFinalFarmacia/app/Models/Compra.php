<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Compra extends Model{
    protected $table = 'modelo_compra';
    protected $fillable = ['fecha','numero_Productos','valor_Total','descripcion','date_created','updated_ad','cliente_id','product_id'
    ];

    public $timestamps = false;
    
    //protected $primaryKey = 'compra_id';
    /*protected $hidden = [
        'cliente_id'
    ];*/
}