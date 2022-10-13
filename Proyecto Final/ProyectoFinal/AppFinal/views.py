from sqlite3 import Cursor
from django.shortcuts import render
from AppFinal.models import *
from django.http import HttpResponse
from AppFinal.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def InicioSesion(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)

            if user:
                login(request, user)

                return render(request, "AppFinal/inicio.html", {"mensaje": f"Bienvenido {user}"})

        else:

            return render(request, "AppFinal/inicio.html", {"mensaje": "Datos incorrectos."})

    else:

        form = AuthenticationForm()
    
    return render(request, "AppFinal/login.html",{"formulario": form})

def registro(request):

    if request.method == "POST":
        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppFinal/inicio.html", {"mensaje":"Usuario creado."})

    else: 
        form = UsuarioRegistro()
    
    return render(request, "AppFinal/registro.html", {"formulario":form})


@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info ["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            

            usuario.save()

            return render(request, "AppFinal/inicio.html")
    
    else:

        form = FormularioEditar(initial={

            "email":usuario.email,
            "first_name":usuario.first_name,
            

        })

    return render(request, "AppFinal/editarPerfil.html", {"formulario":form, "usuario":usuario})


def inicio(request):
    
    return render(request, "AppFinal/inicio.html" )

def categoria(request):
    
    return render(request, "AppFinal/categoria.html" )

def cines(request):
    
    return render(request, "AppFinal/cines.html" )

def peliculas(request):
    
    return render(request, "AppFinal/peliculas.html" )

def acercademi(request):
    
    return render(request, "AppFinal/acercademi.html" )

def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioPeliculas(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            peliF = Peliculas(nombre=info["nombre"], duracion=info["duracion"])

            peliF.save()

            return render(request, r"AppFinal/inicio.html")

    else:

        formulario1 = FormularioPeliculas()

    return render(request, "AppFinal/formularioPeli.html", {"form1":formulario1})




def busquedaPelis(request):

    return render(request, "AppFinal/buscarPelis.html")

def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        duracion = Peliculas.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppFinal/resultados.html", {"nombres":nombre, "duracion":duracion})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

@login_required
def leerCines(request):

    cinesf = Cines.objects.all()


    return render(request, "AppFinal/leerCines.html", {"movies": cinesf})

def crearCines(request):

    
    if request.method=="POST":

        formulCines = FormularioCines(request.POST)
        
        if formulCines.is_valid():

            info = formulCines.cleaned_data

            cinesF = Cines(nombre=info["nombre"], ubicacion=info["ubicacion"])

            cinesF.save()

            return render(request, r"AppFinal/inicio.html")

    else:

        formulCines = FormularioCines()

    return render(request, "AppFinal/formularioCines.html", {"formC":formulCines})


def eliminarCines(request, cinesNombre ):

    cines = Cines.objects.get(nombre=cinesNombre)
    cines.delete()

    cinesores = Cines.objects.all()

    contexto = {"movies" : cinesores}

    return render (request, "AppFinal/leerCines.html", contexto)


def editarCines(request, cineNombre):

    cines = Cines.objects.get(nombre=cineNombre)
   
    if request.method == "POST" :

        formulCines = FormularioCines(request.POST)
        
        if formulCines.is_valid():

            info = formulCines.cleaned_data

            cines.nombre = info["nombre"]
            cines.ubicacion = info["ubicacion"]

           

            cines.save()

            return render(request, "AppFinal/inicio.html")

    else:

        formulCines = FormularioCines(initial={"nombre":cines.nombre, "ubicacion":cines.ubicacion})

    return render(request, "AppFinal/editarCines.html", {"formulCines":formulCines, "nombre":cineNombre})


@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatars(usuario = usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppFinal/inicio.html")
        
    else:

        form = AvatarFormulario()
        
    return render(request, "AppFinal/agregarAvatar.html", {"formulario":form})





class PeliculasList(LoginRequiredMixin, ListView):

    model = Peliculas

class PeliculasDetalle(LoginRequiredMixin, DetailView):

    model = Peliculas

class PeliculasCreacion(LoginRequiredMixin, CreateView):

    model = Peliculas
    success_url = "/AppFinal/peliculas/list"
    fields = ['nombre', 'duracion']

class PeliculasUpdate(LoginRequiredMixin, UpdateView):

    model = Peliculas
    success_url = "/AppFinal/peliculas/list"
    fields = ['nombre', 'duracion']

class PeliculasDelete(LoginRequiredMixin, DeleteView):

    model = Peliculas
    success_url = "/AppFinal/peliculas/list"



