from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from producto_app.models import *
from producto_app.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

@login_required
def Productos(request):
    productos_list = Producto.objects.all()
    productos = []

    if request.method == 'POST':
        gett = request.POST.get('ingresoId')
        catego = request.POST.get('CategoriaIngreso')

        if gett:
            gett = gett.upper()
            productos_list = Producto.objects.filter(nombre__contains=gett)
        elif catego:
            productos_list = Producto.objects.filter(fk_categoria=catego)
        else:
            productos_list = Producto.objects.all()

    paginator = Paginator(productos_list, 10)  # Muestra 10 productos por página
    page_number = request.GET.get('page')
    try:
        productos = paginator.page(page_number)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    return render(request, 'productos/ver-productos.html', {'productos': productos})




@login_required
def AñadirProducto(request):
    mensaje = ""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Guarda el producto en la base de datos si el formulario es válido
            if request.user.is_superuser:
                form.save()
                return redirect('http://127.0.0.1:8000/productos/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"

    else:
        form = ProductoForm()

    return render(request, 'productos/add-productos.html', {'form': form, 'mensaje' : mensaje})

@login_required
def EditarProducto(request, usuario_id):
    producto = get_object_or_404(Producto, id=usuario_id)
    mensaje = ""
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario =ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            if request.user.is_superuser:
                formulario.save()
                return redirect('http://127.0.0.1:8000/productos/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"
                
        data['form'] = formulario
        data['mensaje'] = mensaje
    return render(request, 'productos/add-productos.html', data)


def eliminar_producto(request, usuario_id):
    producto = get_object_or_404(Producto, id=usuario_id)
    if request.user.is_superuser:
        producto.delete()
        return redirect('http://127.0.0.1:8000/productos/')
    else:
        messages.error(request, 'No tienes permisos para ejecutar esta acción.')
        return redirect('http://127.0.0.1:8000/productos/')



# Categorias


@login_required
def Categorias(request):
    Categorias = None
    Categorias = Categoria.objects.all()
    return render(request, 'categorias/ver-categorias.html', {'categorias': Categorias})


@login_required
def AñadirCategoria(request):
    mensaje = ""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            if request.user.is_superuser:
                form.save()
                return redirect('http://127.0.0.1:8000/productos/categorias/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"

    else:
        form = CategoriaForm()

    return render(request, 'categorias/add-categorias.html', {'form': form, 'mensaje': mensaje})


@login_required
def eliminar_categoria(request, usuario_id):
    producto = get_object_or_404(Categoria, id=usuario_id)
    if request.user.is_superuser:
        producto.delete()
        return redirect('http://127.0.0.1:8000/productos/categorias/')

    else:
        messages.error(request, 'No tienes permisos para ejecutar esta acción.')
    return redirect('http://127.0.0.1:8000/productos/categorias/')





@login_required
def EditarCategoria(request, usuario_id):
    registro = get_object_or_404(Categoria, id=usuario_id)
    data = {
        'form': CategoriaForm(instance=registro)
    }
    if request.method == 'POST':
        formulario =CategoriaForm(data=request.POST, instance=registro)
        if formulario.is_valid:
            if request.user.is_superuser:
                formulario.save()
                return redirect('http://127.0.0.1:8000/productos/categorias/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"
        data['form'] = formulario
        data['mensaje'] = mensaje
    return render(request, 'categorias/add-categorias.html', data)



# Marca

@login_required
def Marcas(request):
    registros = None
    registros = Marca.objects.all()
    return render(request, 'marcas/ver-marcas.html', {'marcas': registros})


@login_required
def AñadirMarca(request):
    mensaje = ""
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            if request.user.is_superuser:
                form.save()
                return redirect('http://127.0.0.1:8000/productos/marcas/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"
            

    else:
        form = MarcaForm()

    return render(request, 'marcas/add-marcas.html', {'form': form, 'mensaje': mensaje})

@login_required
def Editarmarca(request, usuario_id):
    mensaje = ""
    registro = get_object_or_404(Marca, id=usuario_id)
    data = {
        'form': MarcaForm(instance=registro)
    }
    if request.method == 'POST':
        formulario =MarcaForm(data=request.POST, instance=registro)
        if formulario.is_valid:
            if request.user.is_superuser:
                formulario.save()
                return redirect('http://127.0.0.1:8000/productos/marcas')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"
        data['form'] = formulario
        data['mensaje'] = mensaje
    return render(request, 'marcas/add-marcas.html', data)




@login_required
def eliminar_marca(request, usuario_id):
    producto = get_object_or_404(Marca, id=usuario_id)
    if request.user.is_superuser:
        producto.delete()
        return redirect('http://127.0.0.1:8000/productos/marcas/')
    else:
        messages.error(request, 'No tienes permisos para ejecutar esta acción.')
        return redirect('http://127.0.0.1:8000/productos/marcas/')



# Proveedores
@login_required
def Proveedores(request):
    registros = Proveedor.objects.all()
    ingreso = request.POST.get('ingresoId')
    if request.method =='POST':
        if ingreso:
            registros = Proveedor.objects.filter(nombre__contains = ingreso)
        else:
            registros = Proveedor.objects.all()
    return render(request, 'proveedores/ver-proveedores.html', {'proveedores': registros})

@login_required
def AñadirProveedor(request):
    mensaje = ""
    form = ProveedorForm()  # Crear el formulario en todas las situaciones

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            if request.user.is_superuser:
                form.save()
                return redirect('http://127.0.0.1:8000/productos/proveedores/')
            else:
                mensaje = "No tienes permisos para ejecutar esta acción!"

    return render(request, 'proveedores/add-proveedores.html', {'form': form, 'mensaje': mensaje})


@login_required
def EditarProveedor(request, usuario_id):
    registro = get_object_or_404(Proveedor, id=usuario_id)
    data = {
        'form': ProveedorForm(instance=registro)
    }
    if request.method == 'POST':
        formulario =MarcaForm(data=request.POST, instance=registro)
        if formulario.is_valid:
            if request.user.is_superuser:
                formulario.save()
                return redirect('http://127.0.0.1:8000/productos/proveedores')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"

        data['form'] = formulario
        data['mensaje'] = mensaje
    return render(request, 'proveedores/add-proveedores.html', data)



@login_required
def eliminar_proveedor(request, usuario_id):
    producto = get_object_or_404(Proveedor, id=usuario_id)
    if request.user.is_superuser:
        producto.delete()
        return redirect('http://127.0.0.1:8000/productos/proveedores/')
    else:
        messages.error(request, 'No tienes permisos para ejecutar esta acción.')
        return redirect('http://127.0.0.1:8000/productos/proveedores/')
