import uuid

from django.contrib.gis.db import models


class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    poly = models.PolygonField()

    def __str__(self):
        return f'{id}'


class Courier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
