from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group
from .forms import AutorForm, EditorialForm, LibroForm, UsuarioForm
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

def agregar_libro(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = LibroForm(request.POST)
            if formulario.is_valid():
                libro = formulario.save(commit=False)
                libro.save()
                return redirect('/administrador')
        else:
            formulario=LibroForm()
        return render(request, 'blog/agregar_libro.html', {'formulario':formulario})
    else:
        return redirect('/')

def agregar_editorial(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = EditorialForm(request.POST)
            if formulario.is_valid():
                editorial = formulario.save(commit=False)
                editorial.save()
                return redirect('/administrador')
        else:
            formulario=EditorialForm()
        return render(request, 'blog/agregar_editorial.html', {'formulario':formulario})
    else:
        return redirect('/')

def agregar_usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = UsuarioForm(request.POST)
            if formulario.is_valid():
                if 'groups' in request.POST:
                    grupo=get_object_or_404(Group,pk=request.POST["groups"])
                    usuario = formulario.save(commit=False)
                    usuario.password = make_password(usuario.password)
                    usuario.save()
                    grupo.user_set.add(usuario)
                    return redirect('/')
                else:
                    return render(request, 'blog/agregar_usuario.html', {'formulario':formulario,'mensaje':'Se debe elegir un grupo'})
        else:
            formulario=UsuarioForm()
        return render(request, 'blog/agregar_usuario.html', {'formulario':formulario,'mensaje':''})
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
            formulario=AutorForm(instance=autor)
        return render(request, 'blog/editar_autor.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_libro(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        libro = get_object_or_404(Libro,pk=pk)
        if request.method=="POST":
            formulario = LibroForm(request.POST,instance=libro)
            if formulario.is_valid():
                libro = formulario.save()
                return redirect('/administrador')
        else:
            formulario=LibroForm(instance=libro)
        return render(request, 'blog/editar_libro.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_editorial(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        editorial = get_object_or_404(Editorial,pk=pk)
        if request.method=="POST":
            formulario = EditorialForm(request.POST,instance=editorial)
            if formulario.is_valid():
                editorial = formulario.save()
                return redirect('/administrador')
        else:
            formulario=EditorialForm(instance=editorial)
        return render(request, 'blog/editar_editorial.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        if request.method=="POST":
            formulario = UsuarioForm(request.POST,instance=usuario)
            if formulario.is_valid():
                if 'groups' in request.POST:
                    grupo=get_object_or_404(Group,pk=request.POST["groups"])
                    usuario = formulario.save(commit=False)
                    usuario.password = make_password(usuario.password)
                    usuario.save()
                    grupo.user_set.add(usuario)
                    return redirect('/')
                else:
                    return render(request, 'blog/editar_usuario.html', {'formulario':formulario,'mensaje':'Se debe elegir un grupo'})
        else:
            formulario=UsuarioForm(instance=usuario)
        return render(request, 'blog/editar_usuario.html', {'formulario':formulario,'mensaje':''})
    else:
        return redirect('/')

def eliminar_autor(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        autor = get_object_or_404(Autor,pk=pk)
        autor.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_libro(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        libro = get_object_or_404(Libro,pk=pk)
        libro.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_editorial(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        editorial = get_object_or_404(Editorial,pk=pk)
        editorial.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        usuario.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def administrador(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = request.user
        return render(request,'blog/administrador.html', {'usuario':usuario,})
    else:
        return redirect('/')
def usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        usuario = request.user
        return render(request, 'blog/usuario.html', {'usuario':usuario,})
    else:
        return redirect('/')

def listado_libros_usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        libros=Libro.objects.all()
        return render(request, 'blog/listado_libros_usuario.html', {'libros':libros,})
    else:
        return redirect('/')

def listar_autores(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        autores=Autor.objects.all()
        return render(request, 'blog/listar_autores.html', {'autores':autores,})
    else:
        return redirect('/')

def listar_libros(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        libros=Libro.objects.all()
        return render(request, 'blog/listar_libros.html', {'libros':libros,})
    else:
        return redirect('/')

def listar_editoriales(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        editoriales=Editorial.objects.all()
        return render(request, 'blog/listar_editoriales.html', {'editoriales':editoriales,})
    else:
        return redirect('/')

def listar_usuarios(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuarios=User.objects.all()
        return render(request, 'blog/listar_usuarios.html', {'usuarios':usuarios,})
    else:
        return redirect('/')

def iniciar(request):
    if request.user.is_authenticated():
        if len(request.user.groups.all())>0:
            if request.user.groups.all()[0].name == "Administrador":
                return redirect('/administrador')
            elif request.user.groups.all()[0].name == "Usuario":
                return redirect('/usuario')
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
