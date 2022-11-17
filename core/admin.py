from django.contrib import admin

from .models import Jogador, Jogo, Partida


@admin.register(Jogador)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "num_vitorias",
        "num_derrotas",
        "pontuacao",
    )
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = (
        "nome",
        "pontuacao",
    )
    list_per_page = 25


@admin.register(Partida)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "jogador_1",
        "jogador_2",
    )
    search_fields = (
        "jogador_1",
        "jogador_2",
    )
    list_filter = (
        "jogador_1",
        "jogador_2",
    )
    ordering = (
        "jogador_1",
        "jogador_2",
    )


@admin.register(Jogo)
class EditoraAdmin(admin.ModelAdmin):
    list_display = (
        "pontos_jogador_1",
        "pontos_jogador_2",
        "data",
    )
    search_fields = ("data",)
    list_filter = ("data",)
    ordering = ("data",)
