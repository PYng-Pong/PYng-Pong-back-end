from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import JogadorViewSet, PartidaViewSet, JogoViewSet

router = DefaultRouter()
router.register(r"jogadores", JogadorViewSet)
router.register(r"partidas", PartidaViewSet)
router.register(r"jogos", JogoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]
