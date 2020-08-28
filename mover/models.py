from django.db import models
from django.contrib.auth.models import AbstractUser


class Mover(AbstractUser):
    about = models.CharField(max_length=5000, blank=True, null=True, help_text="About me section")
