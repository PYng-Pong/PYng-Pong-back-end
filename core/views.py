from rest_framework.viewsets import ModelViewSet

from core.models import Jogador, Partida, Jogo
from core.serializers import (
    JogadorSerializer,
    PartidaSerializer,
    JogoSerializer,
    JogoDetailSerializer,
)


class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer


class PartidaViewSet(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer


class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return JogoDetailSerializer
        return JogoSerializer
