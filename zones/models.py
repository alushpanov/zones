import uuid

from django.contrib.gis.db import models


class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    coordinates = models.PolygonField()

    def __str__(self):
        return f'{self.id}'


class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, blank=True, null=True, related_name='couriers')

    def __str__(self):
        return self.name
