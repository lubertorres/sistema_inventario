from django.db import models


from estado_app.models import Estado

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null = False, default=None)
    descripcion = models.CharField(max_length=50, null=False)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre
    




class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null = False, default=None)
    descripcion = models.CharField(max_length=50, null=False)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre
    

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null = False, default=None)
    descripcion = models.CharField(max_length=50, null=False)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null = False, default=None)
    descripcion = models.CharField(max_length=255, null = False, default=None)
    fk_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=None)
    fk_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=None)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    stock = models.PositiveIntegerField(default = None)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre

