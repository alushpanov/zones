from rest_framework.routers import SimpleRouter

from zones.api.views import ZoneViewSet


router = SimpleRouter()
router.register('zones', ZoneViewSet, basename='zones')

urlpatterns = []
urlpatterns += router.urls
