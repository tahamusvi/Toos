from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
from rest_framework import status
from .models import *
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
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def course_get(request,kind):
#     try:
#         course = Course.objects.filter(kind__code=kind)
#     except Course.DoesNotExist:
#         return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     ser_data = courseSerializers(course, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
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
def Package_get(request):
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
def Suggested_course(request,phoneNumber):
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
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def course_sagesst(request,grade,kind):
#     try:
#         course = Course.objects.filter(kind_course__pk=kind,grade__pk=grade)
#     except Course.DoesNotExist:
#         return Response({'error': 'this courses does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     ser_data = courseSerializers(course, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def
