from django.shortcuts import render, get_object_or_404
from .models import Event,SubEvent

# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request,'events/event.html',{'events':events})


def sub_events(requests,id):
    event = get_object_or_404(Event, id=id)
    sub_events = SubEvent.objects.filter(event__id=id)
    return render(requests,'events/sub_event.html',{'sub_events':sub_events,'event':event})
