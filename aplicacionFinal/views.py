from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    return render(request, 'aplicacionFinal/index.html')


# ----------- Productos -----------

# Librería

class LibreriaList(LoginRequiredMixin, ListView):

    model = Libreria

class LibreriaCreate(LoginRequiredMixin, CreateView):

    model = Libreria
    fields = ["nombre_producto", "precio", "stock"]
    success_url = reverse_lazy("productos_libreria")


class LibreriaUpdate(LoginRequiredMixin, UpdateView):

    model = Libreria
    fields = ["nombre_producto", "precio", "stock"]
    success_url = reverse_lazy("productos_libreria")


class LibreriaDelete(LoginRequiredMixin, DeleteView):

    model = Libreria
    success_url = reverse_lazy("productos_libreria")

# Papel

class PapelList(LoginRequiredMixin, ListView):

    model = Papel

class PapelCreate(LoginRequiredMixin, CreateView):

    model = Papel
    fields = ["marca", "tipo", "tamanio", "gramaje", "stock"]
    success_url = reverse_lazy("productos_papel")

class PapelUpdate(LoginRequiredMixin, UpdateView):

    model = Papel
    fields = ["marca", "tipo", "tamanio", "gramaje", "stock"]
    success_url = reverse_lazy("productos_papel")

class PapelDelete(LoginRequiredMixin, DeleteView):

    model = Papel
    success_url = reverse_lazy("productos_papel")


# Tintas
    
class TintaList(LoginRequiredMixin, ListView):

    model = Tinta

class TintaCreate(LoginRequiredMixin, CreateView):

    model = Tinta
    fields = ["marca", "tipo_tinta", "color", "stock"]
    success_url = reverse_lazy("productos_tinta")

class TintaUpdate(LoginRequiredMixin, UpdateView):

    model = Tinta
    fields = ["marca", "tipo_tinta", "color", "stock"]
    success_url = reverse_lazy("productos_tinta")

class TintaDelete(LoginRequiredMixin, DeleteView):

    model = Tinta
    success_url = reverse_lazy("productos_tinta")

# Apuntes
    
class ApunteList(LoginRequiredMixin, ListView):

    model = Apunte

class ApunteCreate(LoginRequiredMixin, CreateView):

    model = Apunte
    fields = ["materia", "catedra", "stock"]
    success_url = reverse_lazy("productos_apunte")

class ApunteUpdate(LoginRequiredMixin, UpdateView):

    model = Apunte
    fields = ["materia", "catedra", "stock"]
    success_url = reverse_lazy("productos_apunte")

class ApunteDelete(LoginRequiredMixin, DeleteView):

    model = Apunte
    success_url = reverse_lazy("productos_apunte")


# ----------- Clientes -----------

class ClienteList(LoginRequiredMixin, ListView):

    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):

    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin, UpdateView):

    model = Cliente
    fields = ["nombre", "apellido", "telefono", "email"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):

    model = Cliente
    success_url = reverse_lazy("clientes")



# ----------- Empleados -----------

class EmpleadoList(LoginRequiredMixin, ListView):

    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):

    model = Empleado
    fields = ["nombre", "apellido", "usuario", "email", "telefono", "rol"]
    success_url = reverse_lazy("empleados")


class EmpleadoUpdate(LoginRequiredMixin, UpdateView):

    model = Empleado
    fields = ["nombre", "apellido", "usuario", "email", "telefono", "rol"]
    success_url = reverse_lazy("empleados")


class EmpleadoDelete(LoginRequiredMixin, DeleteView):

    model = Empleado
    success_url = reverse_lazy("empleados")





# ----------- Contactos ----------- 

class ContactoList(LoginRequiredMixin, ListView):

    model = Contacto


class ContactoCreate(LoginRequiredMixin, CreateView):

    model = Contacto
    fields = ["nombre_empresa", "telefono_empresa", "email_empresa", "tipo_de_producto"]
    success_url = reverse_lazy("contactos")


class ContactoUpdate(LoginRequiredMixin, UpdateView):

    model = Contacto
    fields = ["nombre_empresa", "telefono_empresa", "email_empresa", "tipo_de_producto"]
    success_url = reverse_lazy("contactos")


class ContactoDelete(LoginRequiredMixin, DeleteView):

    model = Contacto
    success_url = reverse_lazy("contactos")


# ----------- Login, LogOut, Authentication, Registration -----------

def login_request(request):

    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            
            except:
                avatar = "/media/avatares/default.png"

            finally:
                request.session["avatar"] = avatar

            
            return render(request, 'aplicacionFinal/index.html')

        else:

            return redirect(reverse_lazy('login'))
    else:
        mi_form = AuthenticationForm()

    return render(request, 'aplicacionFinal/login.html', {'form' : mi_form})


def register(request):

    if request.method == "POST":
        mi_form = RegistroForm(request.POST)

        if mi_form.is_valid():
            usuario = mi_form.cleaned_data.get("username")
            mi_form.save()

            return redirect(reverse_lazy('home'))
    
    else:
        mi_form = RegistroForm()

    return render(request, 'aplicacionFinal/registro.html', {'form' : mi_form})


# ----------- Editar Perfil, cambiar Clave, Agregar Avatar -----------
@login_required
def edit_profile(request):

    usuario = request.user

    if request.method == "POST":
        mi_form = UserEditForm(request.POST)

        if mi_form.is_valid():
            user = User.objects.get(username=usuario)
            user.email = mi_form.cleaned_data.get("email")
            user.first_name = mi_form.cleaned_data.get("first_name")
            user.last_name = mi_form.cleaned_data.get("last_name")
            user.save()

            return redirect(reverse_lazy('home'))
        
    else:
        mi_form = UserEditForm(instance=usuario)

    return render(request, 'aplicacionFinal/editar_perfil.html', {'form' : mi_form})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):

    template_name = 'aplicacionFinal/cambiar_clave.html'
    success_url = reverse_lazy('home')


@login_required
def agregar_avatar(request):

    if request.method == "POST":
        mi_form = AvatarForm(request.POST, request.FILES)

        if mi_form.is_valid():
            usuario = User.objects.get(username=request.user)

            avatar_viejo = Avatar.objects.filter(user=usuario)

            if len(avatar_viejo) > 0:
                for i in range(len(avatar_viejo)):
                    avatar_viejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=mi_form.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy('home'))
        
    else:
        mi_form = AvatarForm()

    return render(request, 'aplicacionFinal/agregar_avatar.html', {'form' : mi_form})

# ----------- Buscar elementos  -----------

# Librería ----> Función para buscar artículos de librería, ya que son la mayor cantidad

def buscar_articulos(request):

    return render(request, 'aplicacionFinal/buscar.html')

def encontrar_articulos(request):

    if request.GET["buscar"]:

        patron = request.GET["buscar"]
        articulos = Libreria.objects.filter(nombre_producto__icontains=patron)
        contexto = {"articulos" : articulos}

        return render(request, 'aplicacionFinal/libreria.html', contexto)
    
    contexto = {"articulos" : Libreria.objects.all()}

    return render(request, 'aplicacionFinal/libreria.html')

# ----------- Acerca de mi -----------

def acerca_de_mi(request):

    return render(request, 'aplicacionFinal/acerca_de_mi.html')