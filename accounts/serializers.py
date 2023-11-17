from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# -------------------------------------------------------------------------------------------------------------------------------
class EnhancedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...
        return token
# -------------------------------------------------------------------------------------------------------------------------------
class UserSerializersValid(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nationalCode', 'email','firstName', 'lastName', 'password']

    def validate_nationalCode(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("nationalCode must be 10 digits.")
        

        check = int(value[9])
        test = [int(i) for i in value[:9]]
        weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        result = sum(x * y for x, y in zip(test, weights)) % 11

        if result < 2:
            if(check != result):
                raise serializers.ValidationError("nationalCode not valid.")
        else:
            if(check != 11 - result):
                raise serializers.ValidationError("nationalCode not valid.")

        return value
# -------------------------------------------------------------------------------------------------------------------------------
class CodeValidationSerializers(serializers.ModelSerializer):
    email = serializers.CharField()
    code = serializers.CharField()
    class Meta:
        model = User
        fields = ['email', 'code']
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
