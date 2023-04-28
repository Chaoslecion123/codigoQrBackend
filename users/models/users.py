from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from utils.models import BasicModel

class User(BasicModel,AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    addresses = models.TextField('Direccion',null=True)

    is_client = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

    def get_short_name(self):
        return self.username
    