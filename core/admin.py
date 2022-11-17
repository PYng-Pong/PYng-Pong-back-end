from django.contrib import admin

from .models import Jogador, Jogo, Partida

admin.site.register(Jogador)
admin.site.register(Partida)
admin.site.register(Jogo)
