from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *
from course.models import *
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    phoneNumber = models.CharField(unique=True, max_length=11)
    nationalCode = models.CharField(unique=True, max_length=10)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    grade_obj = models.ForeignKey(
        Grade, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.CharField(max_length=100, null=True, blank=True)
    
    code = models.IntegerField(blank=True,null=True)


    REQUIRED_FIELDS = ['nationalCode']
    USERNAME_FIELD = 'phoneNumber'
    objects = MyUserManager()

    def __str__(self):
        return str(self.phoneNumber) + " - " + str(self.firstName) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
            

    @property
    def is_staff(self):
        return self.is_admin
# ----------------------------------------------------------------------------------------------------------------------------
