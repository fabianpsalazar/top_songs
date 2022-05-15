from .views import SongViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'song', SongViewSet)

urlpatterns = router.urls

print('############### All url routes ##############', urlpatterns)


