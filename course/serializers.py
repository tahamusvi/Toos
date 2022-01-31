from rest_framework import serializers
from .models import *


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name", 'text', 'picture', 'school', 'reshte']
# ----------------------------------------------------------------------------------------------------------------------------
class giudeSerializers(serializers.ModelSerializer):
    class Meta:
        model = giude
        fields = ["name", "phone", "title"]
# -------------------------------------------------------------------------------------------------------------------------------
class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title_persion", "title_en", "picture",
                  "link", "video_preview", "grade"]
class KindSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ["title", "picture"]
# -------------------------------------------------------------------------------------------------------------------------------
class soalSerializers(serializers.ModelSerializer):
    class Meta:
        model = soal
        fields = ["question", "answer"]
