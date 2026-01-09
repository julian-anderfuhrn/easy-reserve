from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "home.html")


@login_required
def dashboard_view(request):
    print(request.user.profile)
    if request.user.profile.role == "PROFESSIONAL":
        return render(request, "dashboard_pro.html")
    else:
        return render(request, "dashboard_patient.html")
