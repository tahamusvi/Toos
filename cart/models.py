from django.db import models
from course.models import *
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator


# ----------------------------------------------------------------------------------------------------------------------------
class Coupon(models.Model):
    code = models.CharField(max_length=30,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code

# ----------------------------------------------------------------------------------------------------------------------------
class Cart(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_peyment = models.TextField()
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True,null=True,default=None)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user} - {self.id}'

    def get_total_price(self):
        total = sum(item.price for item in self.items.all())
        if self.discount:
            discount_price = (self.discount/100)* total
            return total - discount_price
        return total
# ----------------------------------------------------------------------------------------------------------------------------
class Stuff(models.Model):
     title = models.TextField()
     price = models.IntegerField(blank=True, null=True)
     id_course = models.IntegerField(blank=True, null=True)
     course = models.ForeignKey(Course,blank=True, null=True, on_delete=models.CASCADE)
     cart = models.ForeignKey(Cart,blank=True, null=True, on_delete=models.CASCADE,related_name='stuff')

     def __str__(self):
         return str(self.title)
