from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Event,SubEvent,Attendee

# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request,'events/event.html',{'events':events})


def sub_events(requests,id):
    event = get_object_or_404(Event, id=id)
    sub_events = SubEvent.objects.filter(event__id=id)
    return render(requests,'events/sub_event.html',{'sub_events':sub_events,'event':event})


@require_POST
@login_required
def add_to_attendees(request,sub_event_id):
    sub_event = SubEvent.objects.get(id=sub_event_id)

    if Attendee.objects.filter(subevent=sub_event, user=request.user).exists():
        return HttpResponse("Already joined")

    Attendee.objects.create(subevent=sub_event, user=request.user)
    return HttpResponse("Joined")

