from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from services.models import Service, ServiceCategory
from schedules.models import Schedule
from django.contrib.auth.decorators import login_required

# Create your views here.


def service_list(request):
    services = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects

    context = {"services": services, "categories": categories}

    return render(request, "appointments/service_list.html", context)


def availability_view(request, pk):
    service = get_object_or_404(Service, pk=pk, is_active=True)

    schedules = Schedule.objects.filter(service=pk, owner=service.owner, is_active=True)

    return render(
        request,
        "appointments/availability.html",
        {
            "service": service,
            "schedules": schedules,
        },
    )
