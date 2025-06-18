from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    # Rutas locales
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="detail"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>/", views.delete_pokemon, name="delete_pokemon"),

    # Rutas extra de la rama remota (opcional)
    path("<str:nombre>/", views.pokemon_por_nombre, name="detalle_pokemon"),
    path("entrenadores/", views.lista_entrenadores, name="lista_entrenadores"),
    path("entrenadores/<int:trainer_id>/", views.detalle_entrenador, name="detalle_entrenador"),
]
