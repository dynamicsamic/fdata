from django.db import models


class Circuit(models.Model):
    circuit_id = models.IntegerField(primary_key=True)
    cicuit_ref = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.SmallIntegerField()
    url = models.URLField()
