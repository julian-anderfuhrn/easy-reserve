from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class DoctorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.role != "PROFESSIONAL":
            return redirect("core:home")
        return super().dispatch(request, *args, **kwargs)
