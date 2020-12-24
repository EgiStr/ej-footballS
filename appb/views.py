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
    print(request.user.id)
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect("app:login")


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
            return redirect("app:login")
    else:
        form = UserForm()
        context = {
            "form": form
        }
        return render(request, 'register.html', context)

    return render(request, 'register.html', context)


def userlogin(request):
    form = UserForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:index')
            else:
                return render(request, 'login.html', {'error': True})

        elif request.POST.get('submit') == 'sign_up':
            form = UserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')
                user = form.save()

                return render(request, 'login.html')

            else:
                return render(request, 'login.html', {'error': True})
        else:
            return render(request, 'login.html', {'error': True})

    return render(request, 'login.html', context)


def settingProfil(request):
    users = request.user.costumer
    form = FormUser(instance=users)
    profil = Costumer.objects.get(user=request.user)
    if request.method == "POST":
        form = FormUser(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
            context = {
                "profil": profil,
                'form': form,
            }
            return redirect("app:setting")

    context = {
        "profil": profil,
        'form': form,
    }
    return render(request, 'setting.html', context)
