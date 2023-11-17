from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,email,nationalCode,password):
        if not email:
            raise ValueError('users must have email')
        if not nationalCode:
            raise ValueError('users must have National Code')

        user = self.model(nationalCode=nationalCode,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,nationalCode,password):
        user = self.create_user(email,nationalCode,password)
        user.is_admin = True
        user.save(using=self._db)
        return user
