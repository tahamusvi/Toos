from rest_framework import serializers
from .models import *


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name", 'reshte_text', 'picture', 'school', 'kind']
# ----------------------------------------------------------------------------------------------------------------------------
class giudeSerializers(serializers.ModelSerializer):
    class Meta:
        model = giude
        fields = ["name", "phone", "title"]
# -------------------------------------------------------------------------------------------------------------------------------
class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title_persion", "title_en", "picture","grade","code","price","teacher_name","path","count_session","time"]
# -------------------------------------------------------------------------------------------------------------------------------
class KindSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ["title", "picture","code","package_title"]
# -------------------------------------------------------------------------------------------------------------------------------
class soalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["question", "answer"]
# -------------------------------------------------------------------------------------------------------------------------------
class CoverSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ["picture", "title"]
# -------------------------------------------------------------------------------------------------------------------------------
class SessionSerializer(serializers.ModelSerializer):  
   class Meta:
      model = Session_coruse
      fields = ['title','text']
# -------------------------------------------------------------------------------------------------------------------------------
class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["show_title", "picture","code","path"]
        ordering = ('code',)
