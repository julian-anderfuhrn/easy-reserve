from django.db import models
from django.contrib.auth.models import User
from schedules.models import Schedule


class Appointment(models.Model):

    STATUS_AVAILABLE = "canceled"
    STATUS_RESERVED = "reserved"
    STATUS_COMPLETED = "completed"
    STATUS_NO_SHOW = "no_show"

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Canceled"),
        (STATUS_RESERVED, "Reserved"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_NO_SHOW, "No Show"),
    ]

    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, related_name="appointments"
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointments",
    )

    date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]
        unique_together = ("schedule", "date", "start_time")

    def __str__(self):
        return f"{self.schedule.service.name} | {self.date} {self.start_time}-{self.end_time}"
