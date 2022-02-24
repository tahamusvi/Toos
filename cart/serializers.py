from rest_framework import serializers
from .models import *
from extends.National_code_validation import Authenticated_National_Code
# -------------------------------------------------------------------------------------------------------------------------------
class CouponSerializer(serializers.ModelSerializer):
    Code = serializers.CharField()

# -------------------------------------------------------------------------------------------------------------------------------
class StuffSerializer(serializers.ModelSerializer):
    phoneNumber = serializers.CharField()
    class Meta:
        model = Stuff
        fields = ['price', 'title','id']
