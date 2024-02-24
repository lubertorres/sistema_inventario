from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistroForm
from django.views.generic import FormView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import OlvideContrasenaForm

# Create your views here.


@login_required
def home(request):

    #Crear en el modelo TURNO un registro cada vez que se haga el inicio de sesion para controlar los turnos del personal
    usuario = ""
    if request.user.is_authenticated:
        usuario = request.user
        nombre_de_usuario = usuario.username
    return render(request, 'home/home.html', {'usuario': usuario})



def salir(request):
#Actualizar el campo fecha_salida del modelo TURNO con la fecha actual para salida de turno al cerrar la sesion

    logout(request)
    return redirect('/')






def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario al inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})








class OlvideContrasenaView(PasswordResetView):
    template_name = 'registration/olvide_contrasena.html'
    form_class = OlvideContrasenaForm
    email_template_name = 'registration/restablecer_contrasena.html'
    success_url = '/'



class RestablecerContrasenaView(PasswordResetConfirmView):
    template_name = 'restablecer_contrasena.html'
    success_url = '/'






