from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=60)
    estado_provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    sitioweb = models.URLField()

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
