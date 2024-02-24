from django.db import models
from django.utils import timezone

# Create your models here.

class Turno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default=None)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(auto_now_add=True)
