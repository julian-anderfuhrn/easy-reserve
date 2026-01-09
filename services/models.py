from django.db import models
from django.contrib.auth.models import User


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Service categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField(
        help_text="Duration of the appointment in minutes"
    )

    category = models.ForeignKey(
        ServiceCategory, on_delete=models.PROTECT, related_name="services"
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
