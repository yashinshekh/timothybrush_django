from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from timothybrush_django.users.managers import UserManager


class User(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.id})


    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    prov = models.CharField(max_length=100)
    postal = models.CharField(max_length=10)

    show_n_shine_participation = models.BooleanField(default=False)
    poker_run_participation = models.BooleanField(default=False)
    cruise_night_participation = models.BooleanField(default=False)
    street_dance_participation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fname} {self.lname}'s Profile"



class Vehicle(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='vehicles')
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Merchandise(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='merchandise')
    item_type = models.CharField(max_length=100)
    size = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.item_type} - {self.size} {self.color}"



# from django.db import models
#
# class Registration(models.Model):
#     # Personal Information
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email_address = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#     street_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     province_state = models.CharField(max_length=100)
#     postal_zip_code = models.CharField(max_length=10)
#
#     # Vehicle Information
#     year = models.IntegerField()
#     make = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     # Events - These could be BooleanFields or you could use a ManyToManyField for a more complex setup
#     show_n_shine = models.BooleanField(default=False)
#     poker_run = models.BooleanField(default=False)
#     cruise_night = models.BooleanField(default=False)
#     street_dance = models.BooleanField(default=False)
#
#     # Pre-ordering Prices - Assuming quantity for simplicity
#     t_shirts_quantity = models.IntegerField(default=0)
#     toques_quantity = models.IntegerField(default=0)
#     baseball_caps_quantity = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}'s Registration"
