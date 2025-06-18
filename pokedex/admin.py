from django.contrib import admin
from .models import Pokemon

# Si también tienes un modelo llamado Trainer, lo registramos
try:
    from .models import Trainer
    admin.site.register(Trainer)
except ImportError:
    pass

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass
