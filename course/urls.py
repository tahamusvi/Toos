from django.urls import path, include
from .views import *

urlpatterns = [
    path('teachers/', teachers_get, name='teachers_get'),
    path('giude/', giude_get, name='giude'),
    path('courses/<slug:code>/', course_get, name='course_get'),
    path('kinds/', kind_get, name='kind_get'),
    path('questions/', soal_get, name='soal_get'),
]
