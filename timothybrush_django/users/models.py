from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from timothybrush_django.users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    street_address = models.CharField(_("Street Address"), max_length=255,default='')
    city = models.CharField(_("City"), max_length=100,default='')
    province_state = models.CharField(_("Province/State"), max_length=2,default='')
    postal_code = models.CharField(_("Postal/Zip Code"), max_length=20,default='')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.id})
