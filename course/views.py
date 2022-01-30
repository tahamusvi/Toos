from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
from rest_framework import status
from .models import Teacher

danial = 'fdgfdhj67867sdfsf2343nh'


@api_view(['GET'])
@permission_classes([AllowAny])
def teachers_get(request):
    # try:
    #     user = User.objects.get(phoneNumber=phoneNumber)
    # except User.DoesNotExist:
    #     return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    teachers = Teacher.objects.all()

    ser_data = TeacherSerializers(teachers, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------------------------------------------------------------------


@api_view(['POST'])
@permission_classes([AllowAny])
def giude_get(request):
    data = giudeSerializers(data=request.data)
    if data.is_valid():
        g = giude(name=data.validated_data['name'],
                  title=data.validated_data['title'],
                  phone=data.validated_data['phone'])
        g.save()
        return Response({'message': 'ok created!'}, status=status.HTTP_201_CREATED)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def course_get(request, code):
    courses = Course.objects.get(kind_course__code=code)
    ser_data = courseSerializers(courses, many=True)
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
    soals = soal.objects.all()
    ser_data = soalSerializers(soals, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)
