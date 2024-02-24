from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home),
    path('salir', salir),
    path('register/', registro, name='registro'),

    # path('olvide-contrasena/', OlvideContrasenaView.as_view(), name='olvide_contrasena'),

    # path('restablecer-contrasena/<uidb64>/<token>/', RestablecerContrasenaView.as_view(), name='restablecer_contrasena'),


    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),





]