from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.iniciar),
        url(r'^administrador$', views.administrador),
        url(r'^usuario$', views.usuario),
        url(r'^salir$', views.salir),
]
