from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
from rest_framework import status
from .models import *
danial = 'fdgfdhj67867sdfsf2343nh'
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def teachers_get(request):
    teachers = Teacher.objects.all()
    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def giude_get(request):
    data = giudeSerializers(data=request.data)
    if data.is_valid():
        user_giude = giude(name=data.validated_data['name'],
                  title=data.validated_data['title'],
                  phone=data.validated_data['phone'])
        user_giude.save()
        return Response({'message': 'ok created!'}, status=status.HTTP_201_CREATED)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_cover(request):
    covers = Cover.objects.all()
    data = CoverSerializers(covers, many=True)
    return Response(data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def course_get(request,grade,kind):
    try:
        course = Course.objects.filter(kind_course__code=kind,grade__code=grade)
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = courseSerializers(course, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def kind_get(request):
    courses = Kind.objects.all()
    ser_data = KindSerializers(courses, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def soal_get(request):
    soals = Question.objects.all()
    ser_data = soalSerializers(soals, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def one_course_get(request,id):
#     try:
#         course = Course.objects.filter(kind_course__code=kind,grade__code=grade)
#     except Course.DoesNotExist:
#         return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)


# -----------------------------------------------------------------------------------------------------------------------
