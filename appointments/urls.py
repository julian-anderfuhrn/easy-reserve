from django.urls import path
from . import views
from . import api_views

app_name = "appointments"

urlpatterns = [
    path("", views.service_list, name="list"),
    path("<int:pk>/availability/", views.availability_view, name="availability"),
    path(
        "api/service/<int:service_id>/schedules/",
        api_views.available_schedules,
        name="available_schedules",
    ),
]
