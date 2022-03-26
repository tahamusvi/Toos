from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from .models import User
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
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
@api_view(['POST',])
@permission_classes((AllowAny,))
def login_view(request):
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
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': "CSRF cookie set"})
# -------------------------------------------------------------------------------------------------------------------------------
def delete_user():
    users = User.objects.all()
    for user in users:
        if user.is_active == False:
            user.delete()
    return 0
