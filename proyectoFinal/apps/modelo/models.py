from django.db import models

class Cliente(models.Model):
    listaGenero = (
        ('femenino','Femenino'),
        ('masculino', 'Masculino')
    )
    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    genero = models.CharField(max_length = 30, choices = listaGenero, default = 'masculino')
    correo = models.EmailField(max_length = 105, null = False)
    telefono = models.CharField(max_length = 15, null = False)
    direccion = models.TextField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.cedula


class Producto(models.Model):
    producto_id = models.AutoField(primary_key = True)
    codigo = models.IntegerField(unique = True, null = False)
    nombre = models.CharField(max_length = 70, null = False)
    stock = models.IntegerField(unique = True, null = False)
    precio_Unitario = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    date_created = models.DateTimeField(auto_now_add = True)
         
    def __str__(self):
        return self.codigo



class Compra(models.Model):
    compra_id = models.AutoField(primary_key = True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    numero_Productos = models.IntegerField(null = False)
    valor_Total = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    descripcion = models.TextField(default = 'Descripción de la compra')
    product = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    updated_ad = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.compra_id