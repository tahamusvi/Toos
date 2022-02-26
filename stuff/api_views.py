from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
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
@api_view(['POST'])
@permission_classes([AllowAny])
def add_stuff(request):
	info = StuffSerializer(data=request.data)


	if info.is_valid():
		try:
			course = Course.objects.get(title_persion=info.validated_data['title'])
		except Course.DoesNotExist:
			return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)

		try:
			user = User.objects.get(phoneNumber=info.validated_data['phoneNumber'])
			print(user.cart)
		except User.DoesNotExist:
			return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

		if user.cart is None:
			new_cart = Cart(user=user)
			user.cart = new_cart
		  


		stuff = Stuff(title=info.validated_data['title'],
		price=info.validated_data['price'],
		picture = course.picture,
		teacher = course.teacher.name,
		id_course=info.validated_data['id'],
		course = course,
		)

		stuff.cart = user.cart
		stuff.save()
		return Response({'message': 'ok is create'}, status=status.HTTP_201_CREATED)

	else:
		return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def get_total_code(request):
	info = GetTotalPrice(data=request.data)
	if info.is_valid():
		try:
			user = User.objects.get(phoneNumber=info.validated_data['phoneNumber'])
		except User.DoesNotExist:
			return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
		total = user.cart.get_total_price()
		return Response({'total': total}, status=status.HTTP_200_OK)
	else:
		return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_cart(request,phoneNumber):
	try:
		user = User.objects.get(phoneNumber=phoneNumber)
	except User.DoesNotExist:
		return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
	# user.cart.get_total_price()
	# user.cart.save()
	stuff = user.cart.stuff
	data = GetCartPrice(stuff, many=True)

	return Response(data.data, status=status.HTTP_200_OK)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_total(request,phoneNumber):
	try:
		user = User.objects.get(phoneNumber=phoneNumber)
	except User.DoesNotExist:
		return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
	user.cart.save() 
	total = user.cart.get_total_price()
	return Response({'total':total}, status=status.HTTP_200_OK)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def apply_coupon(request,phoneNumber):
	info = ApplyCouponSerializer(data=request.data)
	try:
		user = User.objects.get(phoneNumber=phoneNumber)
	except User.DoesNotExist:
		return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

	if info.is_valid():
		
		try:
			input_coupon = Coupon.objects.get(code=info.validated_data['coupon_text'])
		except Coupon.DoesNotExist:
			return Response({'error': 'this coupon does not exist'}, status=status.HTTP_404_NOT_FOUND)
		if(input_coupon.active):
			user.cart.coupon = input_coupon
			user.cart.save()
			user.save()
			return Response({'message': 'ok is apply'}, status=status.HTTP_200_OK)
		else:
			return Response({'error': 'this coupon is not valid'}, status=status.HTTP_404_NOT_FOUND)
	else:
		return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)