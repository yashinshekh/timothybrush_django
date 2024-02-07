from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Event,SubEvent,Attendee

# Create your views here.
def events(request):
    events = Event.objects.all()
    return render(request,'events/event.html',{'events':events})


def sub_events(request,id):
    event = get_object_or_404(Event, id=id)
    sub_events = SubEvent.objects.filter(event__id=id)

    user_joined_subevents = []
    if request.user.is_authenticated:
        user_joined_subevents = Attendee.objects.filter(
            subevent__in=sub_events,user=request.user
        ).values_list('subevent_id',flat=True)

    context = {
        'event': event,
        'sub_events': sub_events,
        'user_joined_sub_events': user_joined_subevents,
    }

    return render(request,'events/sub_event.html',context)


@require_POST
@login_required
def add_to_attendees(request,sub_event_id):
    sub_event = SubEvent.objects.get(id=sub_event_id)

    if Attendee.objects.filter(subevent=sub_event, user=request.user).exists():
        return HttpResponse("Already joined")

    Attendee.objects.create(subevent=sub_event, user=request.user)
    return HttpResponse("Joined")

