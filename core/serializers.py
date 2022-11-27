from django.contrib.auth.models import Group

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework.serializers import ModelSerializer

from core.models import Jogador, Jogo, Partida


class CustomUserDetailNestedSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ["pk", "username", "first_name", "last_name"]


class JogadorSerializer(ModelSerializer):
    criado_por = CustomUserDetailNestedSerializer()

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
    criado_por = CustomUserDetailNestedSerializer()

    class Meta:
        model = Jogo
        fields = "__all__"
        depth = 1


class CustomRegisterSerializer(RegisterSerializer):
    def save(self, request):
        user = super().save(request)
        user.groups.add(Group.objects.get(name="praticante"))
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("is_active", "is_staff")
