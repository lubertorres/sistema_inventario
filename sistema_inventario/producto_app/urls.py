from django.urls import path
from .views import *


urlpatterns = [
    path('', Productos),
    path('add/', AñadirProducto),
    path('edit/<int:usuario_id>/', EditarProducto),
    path('delete/<int:usuario_id>/', eliminar_producto),


    path('categorias/', Categorias),
    path('categorias/add/', AñadirCategoria),
    path('categorias/edit/<int:usuario_id>/', EditarCategoria),
    path('categorias/delete/<int:usuario_id>/', eliminar_categoria),


    path('marcas/', Marcas),
    path('marcas/add/', AñadirMarca),
    path('marcas/edit/<int:usuario_id>/', Editarmarca),
    path('marcas/delete/<int:usuario_id>/', eliminar_marca),


    path('proveedores/', Proveedores),
    path('proveedores/add/', AñadirProveedor),
    path('proveedores/edit/<int:usuario_id>/', EditarProveedor),
    path('proveedores/delete/<int:usuario_id>/', eliminar_proveedor),


]