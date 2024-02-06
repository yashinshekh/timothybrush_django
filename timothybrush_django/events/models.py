from django.db import models
from django.conf import settings
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # For storing event images
    description = models.TextField()

    def __str__(self):
        return self.name

class SubEvent(models.Model):
    event = models.ForeignKey(Event, related_name='subevents', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='subevent_images/', blank=True, null=True)  # For storing subevent images
    subevent_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_free = models.BooleanField(default=True)  # Indicates if the subevent is free
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Price for paid subevents


    def __str__(self):
        return f"{self.event.name} - {self.name}"

class Attendee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subevent = models.ForeignKey(SubEvent, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'subevent')  # Ensure a user can't register for the same subevent twice

    def __str__(self):
        return f"{self.user} attending {self.subevent}"
