from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.iniciar),
        url(r'^administrador$', views.administrador),
        url(r'^usuario/libros/listado$', views.usuario),
        url(r'^salir$', views.salir),
        url(r'^administrador/libros/agregar_autor$', views.agregar_autor),
]
