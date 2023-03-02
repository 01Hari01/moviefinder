from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.

class UserSignupForm(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(email=self.normalize_email(email), **extra_fields)
