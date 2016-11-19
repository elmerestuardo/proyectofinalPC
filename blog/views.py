from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group
from .forms import AutorForm
from .models import Editorial, Autor, Libro
from django.contrib.auth.hashers import make_password

#def login(request):
#    return render(request, 'blog/login.html', {})

def agregar_autor(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = AutorForm(request.POST)
            if formulario.is_valid():
                autor = formulario.save(commit=False)
                autor.save()
                return redirect('/administrador')
        else:
            formulario=AutorForm()
        return render(request, 'blog/agregar_autor.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_autor(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        autor = get_object_or_404(Autor,pk=pk)
        if request.method=="POST":
            formulario = AutorForm(request.POST,instance=autor)
            if formulario.is_valid():
                autor = formulario.save()
                return redirect('/administrador')
        else:
            formulario=ResultadoForm(instance=resultado)
        return render(request, 'agenda/resultado_modificar.html', {'formulario':formulario})
    else:
        return redirect('/')

def administrador(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuarios = User.objects.all()
        return render(request,'blog/administrador.html', {'usuarios':usuarios,})
    else:
        return redirect('/')
def usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        libros=Libro.objects.all()
        return render(request, 'blog/usuario.html', {'libros':libros,})
    else:
        return redirect('/')

def iniciar(request):
    if request.user.is_authenticated():
        if len(request.user.groups.all())>0:
            if request.user.groups.all()[0].name == "Administrador":
                return redirect('/administrador')
            elif request.user.groups.all()[0].name == "Usuario":
                return redirect('/usuario/libros/listado')
        else:
            logout(request)
            formulario = AuthenticationForm()
            return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'Usuario sin grupo asignado'})
    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            if usuario=='' or clave=='':
                formulario = AuthenticationForm()
                return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'No se completaron todos los campos'})
            else:
                acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    formulario = AuthenticationForm()
                    return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'Usuario no activo'})
            else:
                formulario = AuthenticationForm()
                return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'La combinacion de usuario y contraseña no es correcta'})
        else:
            formulario = AuthenticationForm()
            return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'Relleno de formulario invalido'})
    else:
        formulario = AuthenticationForm()
    return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':''})

def salir(request):
    logout(request)
    return redirect('/')
