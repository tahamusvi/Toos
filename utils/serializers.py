from rest_framework import serializers
from .models import *


class WeekPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeekPlan
        fields = ["title", 'picture', 'kind', 'grade']
# ----------------------------------------------------------------------------------------------------------------------------
