from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from zones.api.serializers import CourierSerializer, ZoneSerializer
from zones.models import Courier, Zone


class ZoneViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):

    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class CourierViewSet(ModelViewSet):

    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
