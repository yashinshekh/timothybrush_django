from django.contrib import admin
from .models import Event,SubEvent,Attendee


admin.site.register(Event)
admin.site.register(SubEvent)
admin.site.register(Attendee)

# Register your models here.
