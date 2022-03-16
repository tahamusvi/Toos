from django.urls import path, include
from .api_views import *


urlpatterns = [
    path('weekplan/<slug:phoneNumber>/',get_WeekPlan),

]
