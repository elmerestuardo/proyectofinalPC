from django import forms
from .models import Editorial,Autor,Libro
from django.contrib.auth.models import User

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre','apellidos','email',)
class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields =('nombre','direccion','ciudad','estado_provincia','pais','sitioweb',)
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields =('titulo','autores','editorial','fecha_publicacion',)
        widgets = {
            'autores':forms.SelectMultiple,
            'editorial': forms.Select,
}
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','groups')
        widgets = {
            'password':forms.PasswordInput,
            'groups': forms.SelectMultiple,
        }
