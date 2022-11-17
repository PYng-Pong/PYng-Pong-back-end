from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from djoser.serializers import (
    UserCreateSerializer as BaseUserRegistrationSerializer,
    UserSerializer,
)

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


class CustomUserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "id",
            "email",
            "username",
            "password",
        )

    def perform_create(self, validated_data):
        user = super().perform_create(validated_data)
        user.groups.add(Group.objects.get(name="praticante"))
        return user


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("id", "username", "email", "is_staff")
