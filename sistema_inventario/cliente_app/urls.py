from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('add/', AñadirCliente),
    path('delete/<int:usuario_id>/', eliminar_cliente),
    path('edit/<int:idCliente>/', editarCliente),
    



]