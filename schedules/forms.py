from django import forms
from .models import Schedule
from core.forms import COMMON_INPUT_CLASSES


class SchedulesForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["day_of_week", "start_time", "end_time"]
        widgets = {
            "day_of_week": forms.Select(attrs={"class": COMMON_INPUT_CLASSES}),
            "start_time": forms.TimeInput(
                attrs={"class": COMMON_INPUT_CLASSES, "type": "time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"class": COMMON_INPUT_CLASSES, "type": "time"}
            ),
        }

    # validations
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("Start time must be before end time")
        return cleaned_data
