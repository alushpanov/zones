from rest_framework.routers import SimpleRouter

from zones.api.views import CourierViewSet, ZoneViewSet


router = SimpleRouter()
router.register('zones', ZoneViewSet, basename='zones')
router.register('couriers', CourierViewSet, basename='couriers')

urlpatterns = []
urlpatterns += router.urls
