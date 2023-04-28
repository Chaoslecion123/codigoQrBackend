from django.db import models
from utils.models import BasicModel
from django.core.validators import RegexValidator


class Client(BasicModel):
    first_name = models.CharField('Nombres',blank=True,max_length=50)
    last_name = models.CharField('Apellidos',blank=True,max_length=50)
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
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,unique=True)

    addresses = models.TextField('Direccion',null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    