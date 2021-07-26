from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, phone, name, type, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, name=name, type=type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone, name, type, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone, name, type, password, **extra_fields)

    def create_superuser(self, email, phone, name, type, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone, name, type, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone'), max_length=13)
    name = models.CharField(_('name'), max_length=100)
    type = models.CharField(_('type'), max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'name', 'type']

    objects = CustomUserManager()


class State(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserData(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    state = models.ForeignKey(State, on_delete=DO_NOTHING)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.name

class UserDocuments(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    aadhar_card = models.ImageField()
    cancelled_check = models.ImageField()

    def __str__(self):
        return self.user.name


class PremiumUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name