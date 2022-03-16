from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(giude)

admin.site.register(Question)
admin.site.register(Cover)

class CoruseAdmin(admin.ModelAdmin):
	def course_sessions_name(self,obj):
		return obj.course_sessions.text
	list_display = ('title_persion','title_en','price','picture','kind')

class KindAdmin(admin.ModelAdmin):
	list_display = ('title','code')
class GradeAdmin(admin.ModelAdmin):
   list_display = ('title','pk')

admin.site.register(Package)
admin.site.register(Course,CoruseAdmin)
admin.site.register(Session_coruse)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Kind,KindAdmin)
