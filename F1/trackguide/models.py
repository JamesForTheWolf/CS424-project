from django.db import models


class Track(models.Model):
    track_name = models.CharField(max_length=100)
    track_length = models.DecimalField(max_digits=5, decimal_places=2)
