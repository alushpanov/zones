import logging

from collections import OrderedDict

from django.contrib.gis.geos import Polygon

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from zones.models import Zone

logger = logging.getLogger(__name__)


class ZoneSerializer(serializers.Serializer):

    id = serializers.UUIDField(read_only=True)
    coordinates = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField(),
            min_length=2,
            max_length=2,
        ),
        min_length=4
    )

    def to_representation(self, instance):
        return OrderedDict(
            id=instance.id,
            coordinates=instance.coordinates.coords[0],
        )

    def validate_coordinates(self, value):
        if value[0] != value[-1]:
            raise ValidationError(
                'The first and the last coordinates must be the same point in order to close the zone'
            )
        return value

    def create(self, validated_data):
        return Zone.objects.create(
            coordinates=Polygon(validated_data['coordinates'])
        )
