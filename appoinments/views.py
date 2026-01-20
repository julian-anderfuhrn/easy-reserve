from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from services.models import Service, ServiceCategory
from django.contrib.auth.decorators import login_required

# Create your views here.


def service_list(request):
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects

    context = {"services": services, "categories": categories}

    return render(request, "appoinments/service_list.html", context)


def availability_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    print(service)
    return render(request, "appoinments/availability_view.html")
