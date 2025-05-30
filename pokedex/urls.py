from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.pokemon, name='detalle_pokemon'),

    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/<int:trainer_id>/', views.detalle_entrenador, name='detalle_entrenador'),
]
