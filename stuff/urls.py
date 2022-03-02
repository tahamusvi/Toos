from django.urls import path, include
from .api_views import *

urlpatterns = [
    path('add/stuff/', add_stuff),
    path('get_total/',get_total_code),
    path('get_cart/<slug:phoneNumber>/',get_cart),
    path('get_total/<slug:phoneNumber>/',get_total),
    path('apply_coupon/<slug:phoneNumber>/',apply_coupon),
    path('test/<slug:phoneNumber>/',test),


    #Zarinpal
    # path('zarin/request/', views.send_request, name='request'),
    # path('zarin/verify/', views.verify , name='verify'),
]
