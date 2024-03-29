from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),

    # ------- Cliente -------
    
    path('clientes/', ClienteList.as_view(), name='clientes'),
    path('cliente_create', ClienteCreate.as_view(), name='cliente_create'),
    path('cliente_update/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente_delete/<int:pk>/', ClienteUpdate.as_view(), name='cliente_delete'),

    # ------- Empleados -------

    path('empleados/', EmpleadoList.as_view(), name='empleados'),
    path('empleado_create/', EmpleadoCreate.as_view(), name='empleado_create'),
    path('empleado_update/<int:pk>/', EmpleadoUpdate.as_view(), name='empleado_update'),
    path('empleado_delete/<int:pk>/', EmpleadoDelete.as_view(), name='empleado_delete'),

    # ------- Productos -------

    # Librería
    path('producto_libreria/', LibreriaList.as_view(), name='productos_libreria'),
    path('producto_libreria_create/', LibreriaCreate.as_view(), name='productos_libreria_create'),
    path('producto_libreria_update/<int:pk>', LibreriaUpdate.as_view(), name='productos_libreria_update'),
    path('producto_libreria_delete/<int:pk>', LibreriaDelete.as_view(), name='productos_libreria_delete'),

    # Papel
    path('producto_papel/', PapelList.as_view(), name='productos_papel'),
    path('producto_papel_create/', PapelCreate.as_view(), name='productos_papel_create'),
    path('producto_papel_update/<int:pk>', PapelUpdate.as_view(), name='productos_papel_update'),
    path('producto_papel_delete/<int:pk>', PapelDelete.as_view(), name='productos_papel_delete'),

    # Tintas
    path('producto_tinta/', TintaList.as_view(), name='productos_tinta'),
    path('producto_tinta_create/', TintaCreate.as_view(), name='productos_tinta_create'),
    path('producto_tinta_update/<int:pk>', TintaUpdate.as_view(), name='productos_tinta_update'),
    path('producto_tinta_delete/<int:pk>', TintaDelete.as_view(), name='productos_tinta_delete'),

    # Apuntes
    path('producto_apunte/', ApunteList.as_view(), name='productos_apunte'),
    path('producto_apunte_create/', ApunteCreate.as_view(), name='productos_apunte_create'),
    path('producto_apunte_update/<int:pk>', ApunteUpdate.as_view(), name='productos_apunte_update'),
    path('producto_apunte_delete/<int:pk>', ApunteDelete.as_view(), name='productos_apunte_delete'),
     

    # ------- Contactos -------

    path('contactos/', ContactoList.as_view(), name='contactos'),
    path('contacto_create/', ContactoCreate.as_view(), name='contacto_create'),
    path('contacto_update/<int:pk>', ContactoUpdate.as_view(), name='contacto_update'),
    path('contacto_delete/<int:pk>', ContactoDelete.as_view(), name='contacto_delete'),

    # ------- Login, LogOut, Registration -------

    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='aplicacionFinal/logout.html'), name='logout'),
    path('registro/', register, name='registrar'),

    # ------- Editar Perfil, cambiar Clave, Agregar Avatar -------

    path('perfil/', edit_profile, name='perfil'),
    path('<int:pk>/password/', CambiarClave.as_view(), name='cambiar_clave'),
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),

    # ------- Buscar -------

    # Librería

    path('buscar_articulos/', buscar_articulos, name='buscar_articulos'),
    path('encontrar_articulos/', encontrar_articulos, name='encontrar_articulos'),


    # ------- Acerca de mi... -------
    path('acerca_de_mi/', acerca_de_mi, name='acerca_de_mi')
]