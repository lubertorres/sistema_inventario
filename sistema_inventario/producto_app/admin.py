from django.contrib import admin

from producto_app.models import *

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Producto)