from django.db import models

from estado_app.models import Estado

# Create your models here.



class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null = False, default=None)
    apellido = models.CharField(max_length=200, null = False, default=None)
    cedula = models.CharField(max_length=10, null = False, default=None)
    correo = models.CharField(max_length=200, null = False, default=None)
    edad = models.PositiveIntegerField(default=None)
    celular = models.CharField(max_length=15, null = False, default=None)
    fk_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre + " " +self.apellido