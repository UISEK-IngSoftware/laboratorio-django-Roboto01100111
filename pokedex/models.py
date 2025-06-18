from django.db import models

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    ciudad_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pokemon(models.Model):
    name = models.CharField(max_length=40, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to="pokemon_images", null=True)
    entrenador = models.CharField(max_length=100, null=True)

    # Campos extra de la otra rama (opcional incluirlos si se usan)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    nivel = models.IntegerField(default=1)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes_pokemon/', null=True, blank=True)

    def __str__(self):
        return self.name or self.nombre or "Pokemon"
