from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.pokemon, name='detalle_pokemon'),

    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/<int:trainer_id>/', views.detalle_entrenador, name='detalle_entrenador'),
]
=======

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pokemon>/", views.pokemon, name="pokemon"),
]
>>>>>>> 15fbca3b279d23cc9ee2b191b81ea8a7575611fd
