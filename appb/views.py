from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from .models import Costumer
from .forms import FormUser, UserForm


def index(request):
    """
    docstring
    """
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect("app:logib")


def register(request):
    form = UserForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone = request.POST.get('phone')
            user = form.save()
            group = Group.objects.get(name='costumer')
            user.groups.add(group)
            Costumer.objects.create(
                user=user,
                name=username,
                email=email,
                phone=phone

            )
            return redirect("app:login")
    else:
        form = UserForm()
        context = {
            "form": form
        }
        return render(request, 'register.html', context)

    return render(request, 'register.html', context)


def login(request):
    """
    docstring
    """
    if request.method == "POST":
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:index')
        else:

            return redirect("app:login")
    return render(request, 'login.html')


def settingProfil(request):
    users = request.user.costumer
    form = FormUser(instance=users)
    profil = Costumer.objects.filter(user=request.user)
    if request.method == "POST":
        form = FormUser(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()

    context = {
        "profil": profil,
        'form': form,
    }
    return render(request, 'setting.html', context)
