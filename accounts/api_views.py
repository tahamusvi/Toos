from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from .models import User
from rest_framework import status
from stuff.models import Cart,Department
from course.models import Grade
from random import randint
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
import json
VALIDATION_CODE = 'fdgfdhj67867sdfsf2343nh'
Sms_link = 'http://www.0098sms.com/sendsmslink.aspx?FROM=300057341485&TO=phoneNumber&TEXT=کد+:+code&USERNAME=smsa5429&PASSWORD=66578289&DOMAIN=0098'
# -------------------------------------------------------------------------------------------------------------------------------
"""
api's in api_views.py :

1-change_password --> change user password
2-user_create  --> create one account with phoneNumber & National Code
3-code_get --> get code for Account validation
4-user_update --> fill other information the user
5-user_get --> get info user

api's in login.py :
1-login --> login user

api's in view.py :
1-login --> login user
2- GetCSRFToken --> get crrf token for login
3-delete_user --> delete deactive account

"""
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_create(request):
    """
        Create User with Post Api

        Sample json :
        {
        "phoneNumber" : "09303016386",
        "nationalCode" : "0110073754"
        }

    """

    info = UserSerializersValid(data=request.data)
    code = randint(1000, 9999)

    if info.is_valid():
        User(nationalCode=info.validated_data['nationalCode'],
             phoneNumber=info.validated_data['phoneNumber'],
             is_active=False,
             code=code).save()
        # send Code to User
        # temp = Sms_link.replace("phoneNumber",info.validated_data['phoneNumber'])
        # temp = temp.replace("code",str(code))
        # response = requests.get(temp)
        return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def user_update(request, phoneNumber):
    """
    1. Update User information
    2. activate accounts
    3. create Cart for user

     Sample json :
     {
         "firstName" : "Taha",
        "lastName" : "Mousavi",
        "password" : "1234gg5678",
        "grade" : "دهم"
     }

    """
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    info = UserSerializersUpdate(user, data=request.data)
    # info = UserSerializersUpdate(data=request.data)


    if info.is_valid():
        user.firstName = info.validated_data['firstName']
        user.lastName = info.validated_data['lastName']
        grade = info.validated_data['grade']
        user.grade_obj = Grade.objects.get(title=grade)
        user.grade = user.grade_obj.title
        user.is_active = True
        user.set_password(info.validated_data['password'])
        cart = Cart(user=user)
        cart.save()
        user.cart = cart
        department = Department(user=user)
        department.save()
        user.department = department
        user.save()
        return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def change_password(request, phoneNumber):
    """
    Change User password with old password

    password --> new password
    VALIDATION_CODE --> Just for more security

     Sample json :
     {
         "old_password" : "1234gg5678",
         "VALIDATION_CODE" : "fdgfdhj67867sdfsf2343nh",
         "password" : "1"
     }

    """

    info = ChangePasswordSerializersValid(data=request.data)
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if info.is_valid():
        if user.check_password(info.validated_data['old_password']):
            user.set_password(info.validated_data['password'])
            VALIDATION_CODE_FRONT = info.validated_data['VALIDATION_CODE']
            if VALIDATION_CODE_FRONT == VALIDATION_CODE:
                user.save()
                return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'validation code is not true'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message': 'old password is not true'}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def change_password_without_old(request, phoneNumber):
    """
    Change User password without old password

    password --> new password
    VALIDATION_CODE --> Just for more security

     Sample json :
     {
         "VALIDATION_CODE" : "fdgfdhj67867sdfsf2343nh",
         "password" : "1"
     }

    """
    info = ChangePasswordWithOutOldSerializersValid(data=request.data)
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if info.is_valid():
        user.set_password(info.validated_data['password'])
        VALIDATION_CODE_FRONT = info.validated_data['VALIDATION_CODE']
        if VALIDATION_CODE_FRONT == VALIDATION_CODE:
            user.save()
            return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'validation code is not true'}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def code_get(request, phoneNumber):
    """
    Get code for authentication
    empty json -->
     Sample json :
     {  }
    """
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
        # temp = Sms_link.replace("phoneNumber",info.validated_data['phoneNumber'])
        # temp = temp.replace("code",str(code))
        # response = requests.get(temp)
        return Response({'message': 'ok', 'code': f'{code}'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def user_get(request, phoneNumber):
    """
    Get User info like Name for FrontEnd(React)
    """
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = UserSerializersInfo(user)
    return Response(ser_data.data, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['POST',])
@permission_classes((AllowAny,))
def login_view(request):
    """
    POST API for login

    Sample json :
    {
        "username" : "09303016386",
        "password" : "1234ff5678"
    }


    """
	#get username and password from POST request post
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    #validate to user is available
    if username is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter username"
            }
        }, status=400)
    elif password is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter password"
            }
        }, status=400)

    # authentication user
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"success": "User has been logged in"})
    return JsonResponse(
        {"errors": "Invalid credentials"},
        status=400,
    )
# -------------------------------------------------------------------------------------------------------------------------------
@method_decorator(ensure_csrf_cookie, name='dispatch')
class get_csrf_token(APIView):
    """
        Get And Set csrf cookie for FrontEnd(React)
    """
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': "CSRF cookie set"})
# -------------------------------------------------------------------------------------------------------------------------------
def delete_user():
    """
        Delete Inactive Users
    """
    users = User.objects.all()
    for user in users:
        if user.is_active == False:
            user.delete()
    return 0
