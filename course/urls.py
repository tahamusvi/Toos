from django.urls import path, include
from .views import *

urlpatterns = [
    path('teachers/', teachers_get, name='teachers_get'),
    path('courses/<slug:kind>/', course_get, name='course_get'),
    path('kinds/<slug:package_code>/', kind_get, name='kind_get'),
    path('package/',Package_get,name="Package_get"),
    path('course/<slug:pk>/',one_course_get,name='one_course_get'),
    path('teachers/<slug:pk>/', teachers_kind_get, name='teachers_kind_get'),
    path('get_session/<slug:code>/', session_get),
    path('onlineClass_get/',onlineClass_get),
    path('is_buy/<slug:phoneNumber>/<slug:code>/',is_buy,name='is_buy'),
    path('suggested_course/<slug:phoneNumber>/',Suggested_course,name='Suggested_course'),
    path('user_courses/<slug:phoneNumber>/',user_courses,name='user_courses'),
    path('fresh_course/',fresh_course,name='fresh_course'),
]
