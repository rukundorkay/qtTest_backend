import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from utils.validators import validate_password_complexity

class CustomUser(AbstractBaseUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )
    username=None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(
        max_length=128,
        validators=[
            validate_password_complexity
        ],
        null=False,
        blank=False,
        help_text="Password must be 8-16 characters with at least one digit and one letter."
    )
    phone_number = models.CharField(max_length=25, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES, default='other') 
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

class VerifyEmail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    otp = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.email} - {self.otp}'

class ResetPassword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.email} - {self.code}'
        