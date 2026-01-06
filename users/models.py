from django.db import models
from django.contrib.auth.models import User

# This model is used to define the rol of the users(patient or proffesional)


class Profile(models.Model):
    ROLE_CHOICES = (("PATIENT", "Patient"), ("PROFESSIONAL", "Professional"))
    user = models.OneToOneField(User, on_delete=(models.CASCADE))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="PATIENT")
