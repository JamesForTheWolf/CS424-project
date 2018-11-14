from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Track(models.Model):
    track_name = models.CharField(max_length=100)
    track_length = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE,)

