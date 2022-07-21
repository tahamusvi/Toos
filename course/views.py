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
    """
        Get Teachers information
    """
    teachers = Teacher.objects.all()
    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def onlineClass_get(request,phoneNumber):
    """
        gets online class information the user has purchased that courses
    """
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    data = {}
    courses = user.courses.all()
    for course in courses:
        ser_data = OnlineClassSerializers(course.onlineClass, many=True)
        data[course.title_en] = ser_data.data
        break

    for course in courses:
        ser_data.data.append(OnlineClassSerializers(course.onlineClass, many=True))


    return Response(ser_data.data, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def teachers_kind_get(request,pk):
    """
        Gets teachers whose kind code is equal to the kind in url
        codes:
        جامع سالیانه : ۷
        همایش : ۸
        نکته و تست : ۶
        نهم : ۵
        هشتم : ۴
        هفتم : ۳
        یازدهم : ۲
        دهم : ۱
    """
    try:
        teachers = Teacher.objects.filter(pk=pk)
    except Teacher.DoesNotExist:
        return Response({'error': 'this teachers does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def course_get(request,kind):
    """
        Gets courses whose kind code is equal to the kind in url
        codes:
        جامع سالیانه : ۷
        همایش : ۸
        نکته و تست : ۶
        نهم : ۵
        هشتم : ۴
        هفتم : ۳
        یازدهم : ۲
        دهم : ۱
    """
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
    """
        Gets kinds whose package code is equal to the package_code in url
        codes:
        کنکور : ۱
        پایه : ۲
        دوره اول : ۳
    """
    kinds = Kind.objects.filter(package__code=package_code).order_by('code')
    ser_data = KindSerializers(kinds, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def package_get(request):
    """
        Gets packages
    """
    packages = Package.objects.all().order_by('code')
    ser_data = PackageSerializers(packages, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def one_course_get(request,pk):
    """
        Gets course whose code is equal to the pk in url

        example :
        localhost:8000/api/course/98007/

        Response:
        {
        "title_persion": "نکته و تست شیمی",
        "title_en": "chemistry",
        "picture": "/images/5.png",
        ....
        }


    """
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
    """
        Gets courses whose grade is equal to the user's grade
    """
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
    """
        Check the user has purchased the course(code) or not
    """
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
def user_courses(request,phoneNumber):
    """
        Gets the courses that the user has purchased
    """
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
    """
        Gets all courses ordered by date
    """
    fresh_courses = Course.objects.filter(is_new = True).order_by('created')
    ser_data = courseSerializers(fresh_courses, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def session_get(request,code):
    """
        Gets course sessions whose course code is equal to the code in url

        example :
        localhost:8000/api/get_session/98007/

        Response:
        {
            {
                "title": "1",
                "text": "معرفی دوره",
                "link": "link",
                "time": "01:20:00",
                "is_free": false
            },
            {
                "title": "2",
                "text": "استوکیومتری",
                "link": "link",
                "time": "01:40:00",
                "is_free": false
            },
            {
                "title": "3",
                "text": "اسید و باز",
                "link": "link",
                "time": "02:00:00",
                "is_free": false
            }
        }


    """
    try:
        course = Course.objects.get(code = code)
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)

    sessions = course.sessions.all()
    data = SessionSerializer(sessions,many=True)
    return Response(data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def user_courses_online(request,phoneNumber):
#    """
#      This function is out
#    """
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     courses = Course.objects.filter(user = user,is_online = True).order_by('price')
#
#     ser_data = courseSerializers(courses, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
