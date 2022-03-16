from rest_framework import serializers
from .models import User


class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    # password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nationalCode', 'phoneNumber']
# -------------------------------------------------------------------------------------------------------------------------------
class CodeAgainSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []
# -------------------------------------------------------------------------------------------------------------------------------
class ChangePasswordSerializersValid(serializers.ModelSerializer):
    VALIDATION_CODE = serializers.CharField()

    class Meta:
        model = User
        fields = ['password', 'VALIDATION_CODE']
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersUpdate(serializers.ModelSerializer):
    VALIDATION_CODE = serializers.CharField()

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'password', 'grade', 'VALIDATION_CODE']
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'grade',
                  'nationalCode', 'phoneNumber', 'is_admin', 'is_active']
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializerslogin(serializers.ModelSerializer):
    VALIDATION_CODE = serializers.CharField()
    class Meta:
        model = User
        fields = ['password', 'VALIDATION_CODE']
