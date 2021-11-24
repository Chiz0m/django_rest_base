from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail

# Create your models here.
class NewUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_args):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email).lower(),
            **extra_args
        )
        user.set_password(password)
        user.save(using=self._db)

        # send welcome email
        # send_mail(
        #     'Saffespace',
        #     'Here is the message',
        #     'from@saffespace.com',
        #     ['to@test.com'],
        #     fail_silently= False
        # )

        return user

    def create_superuser(self, email, password, **extra_args):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            **extra_args
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(null=True, blank=True, max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # you can add more fields here 
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_attendant = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=40, default="")
    last_name = models.CharField(max_length=50, default="")
    country = models.CharField(max_length=50, default="")
    objects = NewUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']
    
    def __str__(self):
        return self.email