from django.urls import path
from .views import *

urlpatterns = [
    path('',view=events,name='home'),
    path('event/<int:id>',view=sub_events,name='sub_events'),
    path('attend/<int:sub_event_id>',view=add_to_attendees,name='add_to_attendees')
]
