from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html")


def dashboard_view(request):
    print(request.user.profile.role)
    if request.user.profile.role == "PROFESSIONAL":
        return render(request, "dashboard_pro.html")
    else:
        return render(request, "dashboard_patient.html")
