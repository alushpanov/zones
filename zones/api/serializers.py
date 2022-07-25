from collections import OrderedDict

from django.contrib.gis.geos import Polygon, Point

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from zones.models import Courier, Zone


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


class CourierSerializer(serializers.ModelSerializer):

    zone = serializers.PrimaryKeyRelatedField(read_only=True)
    geo_position = serializers.ListField(
        child=serializers.FloatField(),
        min_length=2,
        max_length=2,
        write_only=True,
        required=False,
    )

    class Meta:
        model = Courier
        fields = '__all__'

    @staticmethod
    def _process_geo_position(validated_data):
        courier_pos = validated_data.pop('geo_position', None)
        if courier_pos:
            courier_zone = Zone.objects.filter(
                coordinates__contains=Point(courier_pos)
            ).first()
            validated_data['zone'] = courier_zone

    def update(self, instance, validated_data):
        self._process_geo_position(validated_data)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        self._process_geo_position(validated_data)
        return super().create(validated_data)
