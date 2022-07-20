from rest_framework import serializers
from .models import User

# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nationalCode', 'phoneNumber']
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'password', 'grade']
# -------------------------------------------------------------------------------------------------------------------------------
class ChangePasswordSerializersValid(serializers.ModelSerializer):
    VALIDATION_CODE = serializers.CharField()
    old_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['old_password','password', 'VALIDATION_CODE']
# -------------------------------------------------------------------------------------------------------------------------------
class ChangePasswordWithOutOldSerializersValid(serializers.ModelSerializer):
    VALIDATION_CODE = serializers.CharField()
    class Meta:
        model = User
        fields = ['password', 'VALIDATION_CODE']
# -------------------------------------------------------------------------------------------------------------------------------
class CodeAgainSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []
# -------------------------------------------------------------------------------------------------------------------------------
class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']
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
# -------------------------------------------------------------------------------------------------------------------------------
