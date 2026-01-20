from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    path("", views.service_list, name="list"),
    path("<int:pk>/availability/", views.availability_view, name="availability"),
]
