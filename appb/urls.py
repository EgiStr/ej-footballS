from django.urls import path

from .views import index, settingProfil, logoutUser, userlogin

urlpatterns = [
    path("", index, name="index"),
    path("profil/", settingProfil, name="setting"),
    path("login/", userlogin, name="login"),
    path("logout/", logoutUser, name="logout"),

]
