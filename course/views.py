from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
from rest_framework import status
from .models import *
# -------------------------------------------------------------------------------------------------------------------------------
"""
api's in api_views.py :

1-teachers_get --> get info teacher for frist-page
2-onlineClass_get  --> get link online class
3-teachers_kind_get --> get info teacher for a kind
4-course_get --> get one courses
5-kind_get --> kinds are Grouping of courses
6-Package_get --> package ar grouping of kinds
7-one_course_get --> return course information
8-Suggested_course --> show some course Due to the user grade and kinds
9-is_buy --> check user buy this course or not
10-user_courses --> get corses that user has buy
11-fresh_course --> get new courses
12-session_get --> get one course sessions
"""
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def teachers_get(request):
    teachers = Teacher.objects.all()
    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def onlineClass_get(request):
    #add filter
    onlineClass = OnlineClass.objects.all()
    ser_data = OnlineClassSerializers(onlineClass, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def teachers_kind_get(request,pk):
    try:
        teachers = Teacher.objects.filter(kind__pk=pk)
    except Teacher.DoesNotExist:
        return Response({'error': 'this teachers does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def course_get(request,kind):
    try:
        course = Course.objects.filter(kind__code=kind).order_by('price')
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = courseSerializers(course, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def kind_get(request,package_code):
    kinds = Kind.objects.filter(package__code=package_code).order_by('code')
    ser_data = KindSerializers(kinds, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def package_get(request):
    packages = Package.objects.all().order_by('code')
    ser_data = PackageSerializers(packages, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def one_course_get(request,pk):
    try:
        course = Course.objects.get(code = pk)
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = courseSerializers(course)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def suggested_course(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    suggested_course = Course.objects.filter(grade = user.grade_obj).order_by('price')

    ser_data = courseSerializers(suggested_course, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def is_buy(request,phoneNumber,code):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if user.courses.filter(code = code):
        return Response({'is_free':True}, status=status.HTTP_200_OK)
    return Response({'is_free':False}, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def user_courses_online(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    courses = Course.objects.filter(user = user,is_online = True).order_by('price')

    ser_data = courseSerializers(courses, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def user_courses(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    courses = Course.objects.filter(user = user).order_by('price')
    print(courses)


    ser_data = courseSerializers(courses, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def fresh_course(request):
    fresh_courses = Course.objects.filter(is_new = True).order_by('created')
    ser_data = courseSerializers(fresh_courses, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def session_get(request,code):
    try:
        course = Course.objects.get(code = code)
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)

    sessions = course.sessions.all()
    data = SessionSerializer(sessions,many=True)
    return Response(data.data, status=status.HTTP_200_OK)

# -----------------------------------------------------------------------------------------------------------------------
