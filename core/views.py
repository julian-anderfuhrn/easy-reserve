from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "home.html")


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")
