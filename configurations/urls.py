from django.urls import path

from .views import get_configurations

urlpatterns = [
    path("", get_configurations, name="get_configurations"),
]