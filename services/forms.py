from django import forms
from .models import Service
from core.forms import COMMON_INPUT_CLASSES


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
            "name": forms.TextInput(attrs={"class": COMMON_INPUT_CLASSES}),
            "description": forms.Textarea(
                attrs={"class": COMMON_INPUT_CLASSES, "rows": 4}
            ),
            "duration_minutes": forms.NumberInput(
                attrs={"class": COMMON_INPUT_CLASSES}
            ),
            "category": forms.Select(attrs={"class": COMMON_INPUT_CLASSES}),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                }
            ),
        }
