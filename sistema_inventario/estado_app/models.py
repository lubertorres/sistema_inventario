from django.db import models

# Create your models here.

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.estado