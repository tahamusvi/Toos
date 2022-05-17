from django.contrib import admin
from .models import *

# ----------------------------------------------------------------------------------------------------------------------------
class CartAdmin(admin.ModelAdmin):
	model = Cart
	list_display = ('user','created','total_peyment','paid')
# ----------------------------------------------------------------------------------------------------------------------------
admin.site.register(Cart,CartAdmin)
admin.site.register(Stuff)
admin.site.register(Coupon)
admin.site.register(Receipt)
admin.site.register(Department)
