from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import *
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    """
        main User object that extends django-user
        username --> email

    """
    # phoneNumber = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True)
    nationalCode = models.CharField(unique=True, max_length=10)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    code = models.IntegerField(blank=True,null=True)


    REQUIRED_FIELDS = ['nationalCode']
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return str(self.email) + " - " + str(self.firstName) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
# ----------------------------------------------------------------------------------------------------------------------------
