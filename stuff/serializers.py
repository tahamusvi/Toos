from dataclasses import field
from rest_framework import serializers
from .models import *
# -------------------------------------------------------------------------------------------------------------------------------
class CouponSerializer(serializers.ModelSerializer):
    Code = serializers.CharField()
# -------------------------------------------------------------------------------------------------------------------------------
class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = []
# -------------------------------------------------------------------------------------------------------------------------------
class ReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ["text","Hash_code","pay",'date']
# -------------------------------------------------------------------------------------------------------------------------------
class GetTotalPrice(serializers.ModelSerializer):
	phoneNumber = serializers.CharField()
	class Meta:
		fields = ['phoneNumber',]
# -------------------------------------------------------------------------------------------------------------------------------
class Courseserializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['title_en',]
# -------------------------------------------------------------------------------------------------------------------------------
class GetCartPrice(serializers.ModelSerializer):
	class Meta:
		model = Stuff
		fields = ['title','price','picture','teacher','code']
# -------------------------------------------------------------------------------------------------------------------------------
class GetReceipt(serializers.ModelSerializer):
	class Meta:
		model = Receipt
		fields = ['text','code','Course_Detail','created','pay']
# -------------------------------------------------------------------------------------------------------------------------------
class ApplyCouponSerializer(serializers.ModelSerializer):
	coupon_text = serializers.CharField()
	class Meta:
		model = Cart
		fields = ['coupon_text',]
# -------------------------------------------------------------------------------------------------------------------------------
