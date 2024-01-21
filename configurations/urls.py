from django.urls import path

from .views import get_configurations, get_products, get_disaster_declarations, get_post_loans

urlpatterns = [
    path("configurations/", get_configurations, name="get_configurations"),
    path("products/", get_products, name="get_products"),
    path("disasters/", get_disaster_declarations, name="get_disaster_declarations"),
    path('loans/', get_post_loans, name='get_post_loans'),
]