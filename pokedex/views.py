<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Trainer

# Vista principal: lista todos los Pokémon desde la base de datos
def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

# Vista individual de Pokémon (por ID)
def pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

# Vista lista de entrenadores
def lista_entrenadores(request):
    entrenadores = Trainer.objects.all()
    return render(request, 'lista_entrenadores.html', {'entrenadores': entrenadores})

# Vista detalle de entrenador
def detalle_entrenador(request, trainer_id):
    entrenador = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'detalle_entrenador.html', {'entrenador': entrenador})
=======
from django.http import HttpResponse
from django.template import loader

def index(request):
    pokemons = ['charmander', 'pikachu', 'squirtle']
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon):
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))
>>>>>>> 15fbca3b279d23cc9ee2b191b81ea8a7575611fd
