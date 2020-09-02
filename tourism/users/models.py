from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token  


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,phone_number,password = None):
        if not email:
            raise ValueError("email required")
        if not first_name:
            raise ValueError("first name required")
        if not last_name:
            raise ValueError("last name required")
        if not phone_number:
            raise ValueError("phone number required")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self,email,first_name,last_name,phone_number,password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user





class useraccount(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",
                              max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self,applabel):
        return True

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created = False,**kwargs):
    if created:
        Token.objects.create(user=instance)

