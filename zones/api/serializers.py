import logging

from rest_framework import serializers

from zones.api.fields import CoordinatesField
from zones.models import Zone

logger = logging.getLogger(__name__)


class ZoneSerializer(serializers.Serializer):

    id = serializers.UUIDField(read_only=True)
    area = CoordinatesField()

    def create(self, validated_data):
        return Zone.objects.create(area=validated_data['area'])