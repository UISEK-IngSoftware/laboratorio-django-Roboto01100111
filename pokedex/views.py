from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Pokemon, Trainer
from .forms import PokemonForm

# Página principal
def index(request):
    pokemons = Pokemon.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

# Detalle de un Pokémon por ID
def pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

# Agregar nuevo Pokémon (solo si está autenticado)
@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

# Editar Pokémon existente
def edit_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

# Eliminar Pokémon
def delete_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    pokemon.delete()
    return redirect('pokedex:index')

# Vista de login personalizada
class CustomLoginView(LoginView):
    template_name = "login_form.html"

# Buscar Pokémon por nombre
def pokemon_por_nombre(request, nombre):
    pokemon = get_object_or_404(Pokemon, name=nombre)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

# Lista de entrenadores (si los usas)
def lista_entrenadores(request):
    entrenadores = Trainer.objects.all()
    return render(request, 'lista_entrenadores.html', {'entrenadores': entrenadores})

# Detalle de un entrenador
def detalle_entrenador(request, trainer_id):
    entrenador = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'detalle_entrenador.html', {'entrenador': entrenador})
