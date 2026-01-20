from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Service
from .forms import ServiceForm
from core.mixins import ProfesionalRequiredMixin


class ServiceListView(ProfesionalRequiredMixin, ListView):
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)


class ServiceCreateView(ProfesionalRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "services/service_form.html"
    success_url = reverse_lazy("services:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(ProfesionalRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "services/service_form.html"
    success_url = reverse_lazy("services:list")

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)


class ServiceDeleteView(ProfesionalRequiredMixin, DeleteView):
    model = Service
    template_name = "services/service_confirm_delete.html"
    success_url = reverse_lazy("services:list")

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)
