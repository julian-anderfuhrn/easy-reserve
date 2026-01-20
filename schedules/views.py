from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Schedule
from .forms import SchedulesForm
from core.mixins import ProfesionalRequiredMixin


class ScheduleListView(ProfesionalRequiredMixin, ListView):
    model = Schedule
    template_name = "schedules/schedule_list.html"
    context_object_name = "schedule"

    def get_queryset(self):
        return Schedule.objects.filter(owner=self.request.user)


class ScheduleCreateView(ProfesionalRequiredMixin, CreateView):
    model = Schedule
    form_class = SchedulesForm
    template_name = "schedules/schedule_form.html"
    success_url = reverse_lazy("schedules:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ScheduleUpdateView(ProfesionalRequiredMixin, UpdateView):
    model = Schedule
    form_class = SchedulesForm
    template_name = "schedules/service_form.html"
    success_url = reverse_lazy("schedules:list")

    def get_queryset(self):
        return super().get_queryset()


class ScheduleDeleteView(ProfesionalRequiredMixin, DeleteView):
    model = Schedule
    template_name = "schedules/schedule_confirm_delete.html"
    success_url = reverse_lazy("schedules:list")

    def get_queryset(self):
        return Schedule.objects.filter(owner=self.request.user)
