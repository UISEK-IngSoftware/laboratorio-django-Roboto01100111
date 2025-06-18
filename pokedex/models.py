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
    
    entrenador = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
