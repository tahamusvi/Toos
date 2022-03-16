from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework import status
from accounts.models import User
from .serializers import *
from .models import *
# -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def date_get(request):
#     return Response(, status=status.HTTP_200_OK)
# -------------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_WeekPlan(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    weekplans = WeekPlan.objects.filter(grade=user.grade_obj)

    data = WeekPlanSerializers(weekplans,many = True)
    return Response(data.data, status=status.HTTP_200_OK)
