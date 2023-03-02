from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class UserSignupForm(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email=models.EmailField(max_length=255, unique=True)
    username=models.CharField(max_length=255, unique=True,null=False,blank=False,default="username")
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    password=models.CharField(max_length=200,null=False,blank=False,default="password")
    confirm_password=models.CharField(max_length=200,default="dsfsd",null=False,blank=False)
    objects=UserSignupForm()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    def save(self, *args, **kwargs):
        if self.password==self.confirm_password:
            self.password=make_password(self.password)
            super().save(*args, **kwargs)
        else:
            raise ValueError('Password does not match')
    def set_password(self, raw_password):
        self.password=make_password(raw_password)

