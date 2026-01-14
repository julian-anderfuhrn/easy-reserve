from django.urls import path
from . import views

# Create your tests here.

app_name = "schedules"

urlpatterns = [
    path("", views.ScheduleListView.as_view(), name="list"),
    path("create/", views.ScheduleCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.ScheduleUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ScheduleDeleteView.as_view(), name="delete"),
]
