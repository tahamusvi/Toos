from django.urls import path, include
from .api_views import *
from .views import GetCSRFToken

urlpatterns = [
    path('user/create/', user_create, name='user_create'),
    path('user/update/<slug:phoneNumber>/', user_update, name='user_update'),
    path('user/code/again/<slug:phoneNumber>/', code_get, name='code_get'),
    path('user/change/password/<slug:phoneNumber>/',
         change_password, name='change_password'),
    path('', include('rest_framework.urls')),
    path('user/info/<slug:phoneNumber>/', user_get, name='user_get'),
    path('csrf/', GetCSRFToken.as_view()),
]
