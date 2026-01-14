from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfesionalRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.profile.role != "PROFESSIONAL":
            return redirect("core:home")
        return super().dispatch(request, *args, **kwargs)
