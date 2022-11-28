from rest_framework.viewsets import ModelViewSet

from core.models import Jogador, Jogo, Partida
from core.serializers import (
    JogadorSerializer,
    JogadorDetailSerializer,
    JogoDetailSerializer,
    JogoSerializer,
    PartidaSerializer,
)


class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return JogadorDetailSerializer
        return JogadorSerializer


class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return JogoDetailSerializer
        return JogoSerializer


class PartidaViewSet(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
