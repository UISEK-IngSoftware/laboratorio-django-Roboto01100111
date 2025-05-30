from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

def lista_entrenadores(request):
    entrenadores = Trainer.objects.all()
    return render(request, 'lista_entrenadores.html', {'entrenadores': entrenadores})

def detalle_entrenador(request, trainer_id):
    entrenador = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'detalle_entrenador.html', {'entrenador': entrenador})
def pokemon_por_nombre(request, nombre):
    pokemon = get_object_or_404(Pokemon, nombre=nombre)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})
