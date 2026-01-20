from django import forms
from .models import Service
from core.forms import COMMON_INPUT_CLASSES


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "category",
            "duration_minutes",
            "observation",
            "is_active",
        ]

        widgets = {
            "category": forms.Select(attrs={"class": COMMON_INPUT_CLASSES}),
            "duration_minutes": forms.NumberInput(
                attrs={"class": COMMON_INPUT_CLASSES}
            ),
            "observation": forms.Textarea(
                attrs={"class": COMMON_INPUT_CLASSES, "rows": 4}
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                }
            ),
        }
