from django.contrib.gis.geos import Polygon

from rest_framework.exceptions import ValidationError
from rest_framework_gis.serializers import GeometryField


class CoordinatesField(GeometryField):

    def _validate(self, value):
        for coord in value:
            if not all(isinstance(x, (int, float)) for x in coord):
                raise ValidationError('Coordinates must be of type int or float')

        # Zone must be closed area. It is possible only if the first and the last coordinates are the same point.
        # If they are not, the closing point is added.
        if value[0] != value[-1]:
            value.append(value[0])

    def to_representation(self, value):
        rep = super().to_representation(value)
        return rep['coordinates'][0]

    def to_internal_value(self, value):
        self._validate(value)
        return Polygon(value)
