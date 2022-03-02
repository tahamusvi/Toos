from django.urls import path, include
from .views import *

urlpatterns = [
    path('teachers/', teachers_get, name='teachers_get'),
    path('giude/', giude_get, name='giude'),
    path('courses/<slug:grade>/<slug:kind>/', course_get, name='course_get'),
    path('kinds/', kind_get, name='kind_get'),
    path('questions/', soal_get, name='soal_get'),
    path('covers/', get_cover, name='get_cover'),
    path('course/<slug:id>/',one_course_get,name='one_course_get'),
]
