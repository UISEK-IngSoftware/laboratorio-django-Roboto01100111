from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    nivel = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_pokemon/', blank=True, null=True)

    def __str__(self):
        return self.nombre
class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    ciudad_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
