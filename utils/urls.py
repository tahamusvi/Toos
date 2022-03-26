from django.urls import path, include
from .api_views import *


urlpatterns = [
    path('weekplan/<slug:phoneNumber>/',get_WeekPlan),
    path('covers/', get_cover, name='get_cover'),
    path('giude/', giude_get, name='giude'),
    path('questions/', soal_get, name='soal_get'),
    path('date/',get_date_online,name="get_date_online"),
]
