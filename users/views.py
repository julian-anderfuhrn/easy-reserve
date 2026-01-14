from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            user = User.objects.create_user(
                username=username, email=email, password=password1
            )
            messages.success(request, "Account created successfully")
            login(request, user)
            return redirect("core:home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("core:home")
