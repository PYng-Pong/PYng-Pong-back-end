from django.contrib.auth.models import User
from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=32)
    pontuacao = models.IntegerField(default=0)
    num_vitorias = models.IntegerField(default=0)
    num_derrotas = models.IntegerField(default=0)
    criado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="jogadores"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Jogadores"


class Partida(models.Model):
    jogador_1 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name="partidas_jogador_1"
    )
    jogador_2 = models.ForeignKey(
        Jogador, on_delete=models.PROTECT, related_name="partidas_jogador_2"
    )

    def __str__(self):
        return f"{self.jogador_1} x {self.jogador_2}"


class Jogo(models.Model):
    pontos_jogador_1 = models.IntegerField()
    pontos_jogador_2 = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE, related_name="jogos")
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jogos")

    def __str__(self):
        return f"{self.pontos_jogador_1} x {self.pontos_jogador_2}"
