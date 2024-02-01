from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from payment.models import Account


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValidationError("email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=155, blank=True, null=True)
    last_name = models.CharField(max_length=155, blank=True, null=True)
    image = models.ImageField(upload_to="users/images/")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
