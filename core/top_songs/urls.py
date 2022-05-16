from .views import SongViewSet
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .loginviews import login

router = SimpleRouter()
router.register(r'song', SongViewSet)

urlpatterns = router.urls

urlpatterns += path('login', login),


