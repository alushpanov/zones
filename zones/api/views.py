from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from zones.models import Courier, Zone
from zones.api.serializers import ZoneSerializer


class ZoneViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):

    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
