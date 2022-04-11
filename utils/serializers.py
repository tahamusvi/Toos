from rest_framework import serializers
from .models import *

class CoverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ["picture", "title"]
# -------------------------------------------------------------------------------------------------------------------------------
class WeekPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeekPlan
        fields = ["title", 'picture', 'kind', 'grade']
# ----------------------------------------------------------------------------------------------------------------------------
class giudeSerializers(serializers.ModelSerializer):
    class Meta:
        model = giude
        fields = ["name", "phone", "title"]
# -------------------------------------------------------------------------------------------------------------------------------
class soalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question", "answer"]
# -------------------------------------------------------------------------------------------------------------------------------
