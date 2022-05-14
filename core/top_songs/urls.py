from .views import Test
from django.urls import path


urlpatterns = [
    path('/', Test.as_view()),
]
