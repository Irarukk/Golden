from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.id)+ " " +self.cliente.username+" "+str(self.fecha)[0:16]
    
    
class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    detalle = models.CharField(max_length=90)
    stock = models.IntegerField()
    precio = models.IntegerField()
    oferta = models.BooleanField()
    decto = models.IntegerField()
    imagen =models.CharField(max_length=200) 
    
    
   
    def tachado(self):
        if self.oferta:
            return str(round(self.precio * (1+(self.decto/100))))
        return ""
    
    
    def __str__(self) -> str:
        return self.detalle+" ("+self.codigo+")"
    
class DetalleVenta(models.Model):
    id= models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta , on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return str(self.id)+" "+self.producto.nombre[0:15]+" "+str(self.venta.id)
    
class OrdenCompra(models.Model):
    cliente = models.CharField(max_length=100)
    direccion_envio = models.CharField(max_length=200)
    fecha_compra = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    