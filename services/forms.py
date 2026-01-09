from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
            "description",
            "duration_minutes",
            "category",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
