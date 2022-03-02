from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,phoneNumber,nationalCode,password):
        if not phoneNumber:
            raise ValueError('users must have Phone')
        if not nationalCode:
            raise ValueError('users must have National Code')

        user = self.model(nationalCode=nationalCode,phoneNumber=phoneNumber)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phoneNumber,nationalCode,password):
        user = self.create_user(phoneNumber,nationalCode,password)
        user.is_admin = True
        user.save(using=self._db)
        return user
