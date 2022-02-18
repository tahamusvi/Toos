from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from .models import User
from rest_framework import status
from course.models import Grade
from random import randint
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
# REACT_APP_VALIDATION_CODE = 'fdgfdhj67867sdfsf2343nh'
danial = 'fdgfdhj67867sdfsf2343nh'
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def change_password(request, phoneNumber):
    info = ChangePasswordSerializersValid(data=request.data)
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if info.is_valid():
        user.set_password(info.validated_data['password'])
        danialtex = info.validated_data['danial']
        if danialtex == danial:
            user.save()
        return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_create(request):
    info = UserSerializersValid(data=request.data)
    code = randint(1000, 9999)

    if info.is_valid():
        User(nationalCode=info.validated_data['nationalCode'],
             phoneNumber=info.validated_data['phoneNumber'],
             is_active=False,
             code=code).save()
        # send Code to User
        return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def code_get(request, phoneNumber):
    info = CodeAgainSerializersValid(data=request.data)
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    code = randint(1000, 9999)
    if info.is_valid():
        # send Code to User
        user.code = code
        user.save()
        return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_update(request, phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    info = UserSerializersUpdate(user, data=request.data)

    if info.is_valid():
        user.firstName = info.validated_data['firstName']
        user.lastName = info.validated_data['lastName']
        grade = info.validated_data['grade']
        danialtex = info.validated_data['danial']
        user.grade_obj = Grade.objects.get(title=grade)
        user.grade = user.grade_obj.title
        user.is_active = True
        user.set_password(info.validated_data['password'])
        if danialtex == danial:
            user.save()

        return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def user_get(request, phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = UserSerializersInfo(user)
    return Response(ser_data.data, status=status.HTTP_200_OK)
