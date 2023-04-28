# Generated by Django 4.2 on 2023-04-25 05:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codigoqr', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigoqr',
            name='customers',
            field=models.ManyToManyField(blank=True, related_name='customers', related_query_name='customer', to='users.client'),
        ),
        migrations.AddField(
            model_name='codigoqr',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='workers', related_query_name='worker', to=settings.AUTH_USER_MODEL),
        ),
    ]