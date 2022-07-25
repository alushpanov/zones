from django.contrib.gis.geos import Point

from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from zones.api.serializers import CourierSerializer, ZoneSerializer
from zones.models import Courier, Zone


class ZoneViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):

    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class CourierViewSet(ModelViewSet):

    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='lat',
                type=OpenApiTypes.FLOAT,
                location=OpenApiParameter.QUERY,
                required=True,
            ),
            OpenApiParameter(
                name='lon',
                type=OpenApiTypes.FLOAT,
                location=OpenApiParameter.QUERY,
                required=True,
            ),
        ]
    )
    @action(methods=['get'], detail=False)
    def delivery_zone(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        if lat is None or lon is None:
            raise ValidationError('lat and lon query params must be provided')

        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError:
            raise ValidationError('lat and lon query params must be of type float')

        delivery_pos = Point(lat, lon)
        zone_courier = self.queryset.select_related('zone').filter(
            zone__coordinates__contains=delivery_pos
        ).first()

        if zone_courier:
            return Response(data=self.serializer_class().to_representation(zone_courier))
        else:
            return Response('No couriers currently available in the delivery zone')
