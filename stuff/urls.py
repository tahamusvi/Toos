from django.urls import path, include
from .api_views import *

urlpatterns = [
    path('add/stuff/', add_stuff),
    path('get_total/',get_total_code),
    path('get_cart/<slug:phoneNumber>/',get_cart),
    path('get_total/<slug:phoneNumber>/',get_total),
    path('apply_coupon/<slug:phoneNumber>/',apply_coupon),
]
