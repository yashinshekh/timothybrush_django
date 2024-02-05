from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    TSHIRT = 'tshirt'
    CAP = 'cap'
    TOQUE = 'toque'

    CATEGORY_CHOICES = [
        (TSHIRT, 'T-shirts'),
        (CAP, 'Baseball Caps'),
        (TOQUE, 'Toques'),
    ]

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'
    XXLARGE = 'XXL'

    SIZE_CHOICES = [
        (SMALL, 'S'),
        (MEDIUM, 'M'),
        (LARGE, 'L'),
        (XLARGE, 'XL'),
        (XXLARGE, 'XXL'),
    ]

    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLACK = 'black'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (YELLOW, 'Yellow'),
        (BLACK, 'Black'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=OTHER)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=TSHIRT)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     products = models.ManyToManyField(Product)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Could be calculated
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Order {self.id}"
