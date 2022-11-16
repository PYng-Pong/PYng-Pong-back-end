from rest_framework.serializers import ModelSerializer

from core.models import Jogador, Partida, Jogo


class JogadorSerializer(ModelSerializer):
    class Meta:
        model = Jogador
        fields = "__all__"


class PartidaSerializer(ModelSerializer):
    class Meta:
        model = Partida
        fields = "__all__"


class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = "__all__"


class JogoDetailSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = "__all__"
        depth = 1
