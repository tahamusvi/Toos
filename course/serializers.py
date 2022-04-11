from rest_framework import serializers
from .models import *

# ----------------------------------------------------------------------------------------------------------------------------
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name", "reshte_text", "picture", "school", "kind"]
# ----------------------------------------------------------------------------------------------------------------------------
class OnlineClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = OnlineClass
        fields = ["title", "link"]
# ----------------------------------------------------------------------------------------------------------------------------
class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title_persion", "title_en", "picture","grade","code","price","teacher_name","path","count_session","time","count_user"]
# -------------------------------------------------------------------------------------------------------------------------------
class KindSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ["title", "picture","code","package_title"]
# -------------------------------------------------------------------------------------------------------------------------------
class SessionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Session_coruse
      fields = ["title","text","link",'time']
# -------------------------------------------------------------------------------------------------------------------------------
class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ["show_title", "picture","code","path","icon"]
        ordering = ("code",)
