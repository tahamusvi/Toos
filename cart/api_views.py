from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from .models import User
from rest_framework import status
from course.models import Grade
# REACT_APP_VALIDATION_CODE = 'fdgfdhj67867sdfsf2343nh'
danial = 'fdgfdhj67867sdfsf2343nh'
# -------------------------------------------------------------------------------------------------------------------------------
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def detail(request):
#     cart = Cart(request)
#     return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
# # -------------------------------------------------------------------------------------------------------------------------------
# def detail(request):
#         return Response({'message': 'ok is updated'}, status=status.HTTP_200_OK)
#     return render(request,'cart/detail.html',{'cart':cart})
# ----------------------------------------------------------------------------------------------------------------------------
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def coupon_apply(request,order_id):
#     info = CouponSerializer(data=request.data)
# ----------------------------------------------------------------------------------------------------------------------------
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def stuff_add(request):
#     info = StuffSerializer(data=request.data)
#
#
#     if info.is_valid():
#         try:
#             course = Course.objects.get(id=validated_data['id'],)
#         except Course.DoesNotExist:
#             return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#         stuff = Stuff(title=info.validated_data['title'],
#         title=info.validated_data['title'],
#         price=info.validated_data['price'],
#         id_course=info.validated_data['id'],
#         course = course
#         )
#         try:
#             user = User.objects.get(phoneNumber=validated_data['phoneNumber'])
#         except User.DoesNotExist:
#             return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         stuff.cart = user.cart
#
