from django.urls import path, include
from .api_views import *

urlpatterns = [
    path('add/stuff/<slug:phoneNumber>/<slug:code>/', add_stuff),
    path('get_total/',get_total_code),
    path('get_cart/<slug:phoneNumber>/',get_cart),
    path('get_total/<slug:phoneNumber>/',get_total),
    path('delete/stuff/<slug:phoneNumber>/<slug:code>/',delete_stuff),
    path('apply_coupon/<slug:phoneNumber>/<slug:coupon>/',apply_coupon),
    path('test/<slug:phoneNumber>/',test),
    


    #Zarinpal
    # path('zarin/request/<slug:phoneNumber>/', send_request, name='request'),
    # path('zarin/verify/', verify , name='verify'),
]
