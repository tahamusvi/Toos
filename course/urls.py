from django.urls import path, include
from .views import *

urlpatterns = [
    path('package/',package_get,name="package_get"),
    path('teachers/', teachers_get, name='teachers_get'),
    path('fresh_course/',fresh_course,name='fresh_course'),
    path('courses/<slug:kind>/', course_get, name='course_get'),
    path('kinds/<slug:package_code>/', kind_get, name='kind_get'),
    path('course/<slug:pk>/',one_course_get,name='one_course_get'),
    path('get_session/<slug:code>/', session_get, name='session_get'),
    path('is_buy/<slug:phoneNumber>/<slug:code>/',is_buy,name='is_buy'),
    path('teachers/<slug:pk>/', teachers_kind_get, name='teachers_kind_get'),
    path('user_courses/<slug:phoneNumber>/',user_courses,name='user_courses'),
    path('onlineClass_get/<slug:phoneNumber>/',onlineClass_get, name='onlineClass_get'),
    path('suggested_course/<slug:phoneNumber>/',suggested_course,name='suggested_course'),
    # path('user_courses/online/<slug:phoneNumber>/',user_courses_online,name='user_courses_online'),



]
