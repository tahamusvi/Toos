from rest_framework import serializers
from .models import *
# -------------------------------------------------------------------------------------------------------------------------------
class CouponSerializer(serializers.ModelSerializer):
    Code = serializers.CharField()

# -------------------------------------------------------------------------------------------------------------------------------
class StuffSerializer(serializers.ModelSerializer):
    phoneNumber = serializers.CharField()
    id = serializers.IntegerField()
    class Meta:
        model = Stuff
        fields = ['price', 'title','id','phoneNumber']
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
		fields = ['title','price','picture','teacher']	
# -------------------------------------------------------------------------------------------------------------------------------
class ApplyCouponSerializer(serializers.ModelSerializer):
	coupon_text = serializers.CharField()
	class Meta:
		model = Cart
		fields = ['coupon_text',]	