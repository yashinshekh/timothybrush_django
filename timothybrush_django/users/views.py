from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render, redirect

from .forms import PersonalForm, VechicleForm, EventForm, MemorabiliaForm, PaymentForm, MenstshirtForm

User = get_user_model()


def home(request):
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST)
        if personal_form.is_valid():
            request.session['personal_form_data'] = personal_form.cleaned_data

            vechicle_session_form_data = request.session.get('vechicle_form_data')
            if vechicle_session_form_data:
                vechicle_form = VechicleForm(initial=vechicle_session_form_data)
            else:
                vechicle_form = VechicleForm()

            next_step_html = render_to_string('pages/vechicle_form.html', {'vechicle_form': vechicle_form}, request=request)
            return HttpResponse(next_step_html)
    else:
        personal_session_form_data = request.session.get('personal_form_data')
        if personal_session_form_data:
            personal_form = PersonalForm(initial=personal_session_form_data)
        else:
            personal_form = PersonalForm()

    if request.headers.get('HX-Request', False):
        return render(request, 'pages/personal_form.html', {'personal_form': personal_form})
    else:
        return render(request, 'pages/home.html', {'personal_form': personal_form})


def vechicle_info(request):
    if request.method == "POST":
        vechicle_form = VechicleForm(request.POST)
        if vechicle_form.is_valid():
            request.session['vechicle_form_data'] = vechicle_form.cleaned_data

            event_session_form_data = request.session.get('events_form_data')
            if event_session_form_data:
                event_form = EventForm(initial=event_session_form_data)
            else:
                event_form = EventForm()
            next_step_html = render_to_string('pages/events_form.html',{'event_form':event_form},request=request)
            return HttpResponse(next_step_html)

    else:
        session_form_data = request.session.get('vechicle_form_data')

        print(session_form_data)
        if session_form_data:
            vechicle_form = VechicleForm(initial=session_form_data)
        else:
            vechicle_form = VechicleForm()

    return render(request,'pages/vechicle_form.html',{'vechicle_form':vechicle_form})



def events_info(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            request.session['event_form_data'] = event_form.cleaned_data

            memorabilia_session_form_data = request.session.get('memorabilia_form_data')
            if memorabilia_session_form_data:
                memorabilia_form = MemorabiliaForm(initial=memorabilia_session_form_data)
            else:
                memorabilia_form = MemorabiliaForm()

            next_step_html = render_to_string('pages/memorabilia_form.html', {'memorabilia_form': memorabilia_form}, request=request)
            return HttpResponse(next_step_html)

    else:
        event_form_data = request.session.get('event_form_data')
        if event_form_data:
            event_form = EventForm(initial=event_form_data)
        else:
            event_form = EventForm()

    return render(request, 'pages/events_form.html', {'event_form': event_form})


def memorabilia_info(request):
    if request.method == 'POST':
        memorabilia_form = MemorabiliaForm(request.POST)
        if memorabilia_form.is_valid():
            request.session['memorabilia_form_data'] = memorabilia_form.cleaned_data

            payment_session_form_data = request.session.get('payment_form_data')
            if payment_session_form_data:
                payment_form = PaymentForm(initial=payment_session_form_data)
            else:
                payment_form = PaymentForm()

            next_step_html = render_to_string('pages/payment_form.html', {'payment_form': payment_form}, request=request)
            return HttpResponse(next_step_html)

    else:
        memorabilia_form_data = request.session.get('memorabilia_form_data')
        if memorabilia_form_data:
            memorabilia_form = MemorabiliaForm(initial=memorabilia_form_data)
        else:
            memorabilia_form = MemorabiliaForm()

    # print('here')
    memorabilia_form = MenstshirtForm()
    #
    # print(memorabilia_form)

    return render(request, 'pages/memorabilia_form.html', {'form': memorabilia_form})


def payment_info(request):
    return HttpResponse("Payment is successfull...")



class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()
