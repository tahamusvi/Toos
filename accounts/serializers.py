from rest_framework import serializers
from .models import User
from extends.National_code_validation import Authenticated_National_Code


class UserSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nationalCode', 'phoneNumber']

    # def validate_nationalCode(self,value):
    #     if Authenticated_National_Code(value) == False:
    #         raise serializers.ValidationError('is not right')
    #     return value

# -------------------------------------------------------------------------------------------------------------------------------


class CodeAgainSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []
# -------------------------------------------------------------------------------------------------------------------------------


class ChangePasswordSerializersValid(serializers.ModelSerializer):
    danial = serializers.CharField()

    class Meta:
        model = User
        fields = ['password', 'danial']
# -------------------------------------------------------------------------------------------------------------------------------


class UserSerializersUpdate(serializers.ModelSerializer):
    danial = serializers.CharField()

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'password', 'grade', 'danial']
# -------------------------------------------------------------------------------------------------------------------------------


class UserSerializersInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'grade',
                  'nationalCode', 'phoneNumber', 'is_admin', 'is_active']
# -------------------------------------------------------------------------------------------------------------------------------


class UserSerializerslogin(serializers.ModelSerializer):
    danial = serializers.CharField()

    class Meta:
        model = User
        fields = ['password', 'danial']
