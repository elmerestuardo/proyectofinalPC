from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.iniciar),
        url(r'^administrador$', views.administrador),
        url(r'^administrador/libros/agregar_libro$', views.agregar_libro),
        url(r'^administrador/libros/editar_libro/(?P<pk>[0-9]+)$', views.editar_libro),
        url(r'^administrador/libros/listado$', views.listar_libros),
        url(r'^administrador/libros/eliminar_libro/(?P<pk>[0-9]+)$', views.eliminar_libro),
        url(r'^administrador/editoriales/agregar_editorial$', views.agregar_editorial),
        url(r'^administrador/editoriales/editar_editorial/(?P<pk>[0-9]+)$', views.editar_editorial),
        url(r'^administrador/editoriales/listado$', views.listar_editoriales),
        url(r'^administrador/editoriales/eliminar_editorial/(?P<pk>[0-9]+)$', views.eliminar_editorial),
        url(r'^administrador/usuarios/agregar_usuario$', views.agregar_usuario),
        url(r'^administrador/usuarios/editar_usuario/(?P<pk>[0-9]+)$', views.editar_usuario),
        url(r'^administrador/usuarios/listado$', views.listar_usuarios),
        url(r'^administrador/usuarios/eliminar_usuario/(?P<pk>[0-9]+)$', views.eliminar_usuario),
        url(r'^usuario/libros/listado$', views.listado_libros_usuario),
        url(r'^usuario$', views.usuario),
        url(r'^salir$', views.salir),
        url(r'^administrador/autores/agregar_autor$', views.agregar_autor),
        url(r'^administrador/autores/editar_autor/(?P<pk>[0-9]+)$', views.editar_autor),
        url(r'^administrador/autores/listado$', views.listar_autores),
        url(r'^administrador/autores/eliminar_autor/(?P<pk>[0-9]+)$', views.eliminar_autor),
]
