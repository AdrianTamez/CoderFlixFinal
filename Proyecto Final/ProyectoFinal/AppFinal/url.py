from django.urls import path 
from AppFinal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('categoria', categoria, name="Categorias"),
    path('cines', cines, name="Cines"),
    path('peliculas', peliculas, name="Peliculas"),
    path('acercademi', acercademi, name="yo"),
    path('agregarPeliculas', formulario1 ,name="agregarPeliculas"),
    path('resultados/', resultados ,name="resultadosBusqueda"),
    path('busquedaPelis/', busquedaPelis ,name="buscarPelis"),
    path('login/', InicioSesion, name="Login"),
    path('register/', registro, name="SignUp"),
    path("logout", LogoutView.as_view(template_name="AppFinal/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),
#CRUD PROFESORES
    path("leerCines/", leerCines, name= "leerCines"),
    path("crearCines/", crearCines, name= "crearCines"),
    path("eliminarCines/<cinesNombre>", eliminarCines, name= "eliminarCines"),
    path("editarCines/<cineNombre>", editarCines, name= "editarCines"),

#CRUD PELICULAS METODO FACIL 
    path("peliculas/list/", PeliculasList.as_view() , name= "leerPeliculas"),
    path("peliculas/<int:pk>/", PeliculasDetalle.as_view() , name= "detallePelicula"),
    path("peliculas/crear/", PeliculasCreacion.as_view() , name= "crearPelicula"),
    path("peliculas/editar/<int:pk>/", PeliculasUpdate.as_view() , name= "editarPelicula"),
    path("peliculas/eliminar/<int:pk>/", PeliculasDelete.as_view() , name= "eliminarPelicula"),




]