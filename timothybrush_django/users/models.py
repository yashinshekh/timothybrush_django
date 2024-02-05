from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from timothybrush_django.users.managers import UserManager


class User(AbstractUser):
    PROVINCE_CHOICES = [
        ('AB', 'Alberta'),
        ('BC', 'British Columbia'),
        ('MB', 'Manitoba'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('NS', 'Nova Scotia'),
        ('ON', 'Ontario'),
        ('PE', 'Prince Edward Island'),
        ('QC', 'Quebec'),
        ('SK', 'Saskatchewan'),
    ]


    first_name = models.CharField(max_length=30,default='')
    last_name = models.CharField(max_length=30,default='')
    email = models.EmailField(unique=True)
    street_address = models.CharField(max_length=255,default='')
    city = models.CharField(max_length=100,blank=True,null=True)
    province_state = models.CharField(max_length=2, choices=PROVINCE_CHOICES, blank=True, null=True)
    postal_code = models.CharField(max_length=20,default='')

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.first_name.lower()}{self.last_name.lower()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
