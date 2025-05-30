from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)  # ← AÑADIDO
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_pokemon/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    ciudad_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
