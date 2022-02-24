from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from .models import User

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
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
