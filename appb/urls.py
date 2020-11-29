from django.urls import path

from .views import index, settingProfil

urlpatterns = [
    path("", index, name="index"),
    path("profil/", settingProfil, name="setting")
]
