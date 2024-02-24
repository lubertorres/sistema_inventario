from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from cliente_app.models import *
from cliente_app.forms import CLienteForm

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    Clientes = None
    Clientes = Cliente.objects.all()

    if request.method =='POST':
        gett=request.POST.get('ingresoId')
        if gett:
            Clientes = Cliente.objects.filter(cedula=gett)
        else:
            Clientes = Cliente.objects.all()


    return render(request, 'clientes/ver_clientes.html', {'Clientes': Clientes})

@login_required
def AñadirCliente(request):
    mensaje = ""
    if request.method == 'POST':
        form = CLienteForm(request.POST)
        if form.is_valid():
            formIngreso = form.cleaned_data['cedula']

            cliente = Cliente.objects.filter(cedula=formIngreso).first()
            if cliente == None:        
                mensaje = "Registro exitoso"
                if request.user.is_superuser:
                    form.save()
                    return redirect('http://127.0.0.1:8000/clientes/')
                else:
                    mensaje = "No tienes permisos para ejecutar esta accion!"
            else:
                mensaje = "Usuario ya existe!"

    else:
        form = CLienteForm(initial={'fk_estado': 1})

    return render(request, 'clientes/add-clientes.html', {'form': form, 'mensaje': mensaje})



@login_required
def editarCliente(request, idCliente):
    cliente = get_object_or_404(Cliente, id=idCliente)
    data = {
        'form': CLienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario =CLienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            if request.user.is_superuser:
                formulario.save()
                return redirect('http://127.0.0.1:8000/clientes/')
            else:
                mensaje = "No tienes permisos para ejecutar esta accion!"

        data['form'] = formulario
        data['mensaje'] = mensaje
    return render(request, 'clientes/add-clientes.html', data)



@login_required
def eliminar_cliente(request, usuario_id):
    cliente = Cliente.objects.get(id=usuario_id)
    if request.user.is_superuser:
        cliente.delete()
        return redirect('http://127.0.0.1:8000/clientes/')
    else:
        messages.error(request, 'No tienes permisos para ejecutar esta acción.')
        return redirect('http://127.0.0.1:8000/clientes/')