from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from config.settings.base import PAYPAL_RECEIVER_EMAIL
from django.contrib.auth.hashers import make_password
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.contrib.auth.decorators import login_required

from .forms import PersonalForm, VechicleForm, EventForm, TOSForm, MenstshirtForm,WomenstshirtForm,ToquesForm,BasketballForm
from .models import Profile,Vehicle,Merchandise

User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == 'POST':
            personal_form = PersonalForm(request.POST)
            if personal_form.is_valid():
                request.session['personal_form_data'] = personal_form.cleaned_data
                vechicle_form = VechicleForm(initial=request.session.get('vechicle_form_data')) if request.session.get('vechicle_form_data') else VechicleForm()
                next_step_html = render_to_string('pages/vechicle_form.html', {'vechicle_form': vechicle_form}, request=request)
                return HttpResponse(next_step_html)
        else:
            personal_form = PersonalForm(initial=request.session.get('personal_form_data')) if request.session.get('personal_form_data') else PersonalForm()

        if request.headers.get('HX-Request', False):
            return render(request, 'pages/personal_form.html', {'personal_form': personal_form})
        else:
            return render(request, 'pages/home.html', {'personal_form': personal_form})


def vechicle_info(request):
    if request.method == "POST":
        vechicle_form = VechicleForm(request.POST)
        if vechicle_form.is_valid():
            request.session['vechicle_form_data'] = vechicle_form.cleaned_data
            event_form = EventForm(initial=request.session.get('events_form_data')) if request.session.get('events_form_data') else EventForm()
            next_step_html = render_to_string('pages/events_form.html',{'event_form':event_form},request=request)
            return HttpResponse(next_step_html)
    else:
        vechicle_form = VechicleForm(initial=request.session.get('vechicle_form_data')) if request.session.get('vechicle_form_data')  else VechicleForm()
        return render(request,'pages/vechicle_form.html',{'vechicle_form':vechicle_form})



def events_info(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            request.session['events_form_data'] = event_form.cleaned_data

            mens_form = MenstshirtForm(initial=request.session.get('mens_tshirt_form')) if request.session.get('mens_tshirt_form') else MenstshirtForm()
            womens_form = WomenstshirtForm(initial=request.session.get('womens_tshirt_form')) if request.session.get('womens_tshirt_form') else WomenstshirtForm()
            basketball_form = BasketballForm(initial=request.session.get('basketball_form')) if request.session.get('basketball_form') else BasketballForm()
            toque_form = ToquesForm(initial=request.session.get('toque_form')) if request.session.get('toque_form') else ToquesForm()

            next_step_html = render_to_string('pages/memorabilia_form.html', {
                'menstshirtform': mens_form,
                'womenstshirtform':womens_form,
                'toqueform':toque_form,
                'baseketballform':basketball_form
            }, request=request)
            return HttpResponse(next_step_html)

    else:
        event_form = EventForm(initial=request.session.get('events_form_data')) if request.session.get('events_form_data') else EventForm()
        return render(request, 'pages/events_form.html', {'event_form': event_form})


def memorabilia_info(request):
    if request.method == 'POST':
        mens_tshirt_form = MenstshirtForm(request.POST)
        womens_tshirt_form = WomenstshirtForm(request.POST)
        toques_form = ToquesForm(request.POST)
        basketball_form = BasketballForm(request.POST)

        if mens_tshirt_form.is_valid() and womens_tshirt_form.is_valid() and toques_form.is_valid() and basketball_form.is_valid():

            request.session['mens_tshirt_form'] = mens_tshirt_form.cleaned_data
            request.session['womens_tshirt_form'] = womens_tshirt_form.cleaned_data
            request.session['toque_form'] = toques_form.cleaned_data
            request.session['basketball_form'] = basketball_form.cleaned_data

            tos_form = TOSForm(initial=request.session.get('payment_form_data')) if request.session.get('payment_form_data') else TOSForm()
            next_step_html = render_to_string('pages/tos_form.html', {'payment_form': tos_form}, request=request)
            return HttpResponse(next_step_html)

            # redirect('payment_info')

    else:
        mens_form = MenstshirtForm(initial=request.session.get('mens_tshirt_form')) if request.session.get('mens_tshirt_form') else MenstshirtForm()
        womens_form = WomenstshirtForm(initial=request.session.get('womens_tshirt_form')) if request.session.get('womens_tshirt_form') else WomenstshirtForm()
        basketball_form = BasketballForm(initial=request.session.get('basketball_form')) if request.session.get('basketball_form') else BasketballForm()
        toque_form = ToquesForm(initial=request.session.get('toque_form')) if request.session.get('toque_form') else ToquesForm()


        return render(request, 'pages/memorabilia_form.html', {
            'menstshirtform': mens_form,
            'womenstshirtform':womens_form,
            'toqueform':toque_form,
            'baseketballform':basketball_form
        })


def tos(request):
    if request.method == "POST":
        tos_form = TOSForm(request.POST)
        if tos_form.is_valid():
            return redirect('payment_info')


def payment_info(request):
    event_form_session = request.session.get('events_form_data', {})
    mens_form_session = request.session.get('mens_tshirt_form', {})
    womens_form_session = request.session.get('womens_tshirt_form', {})
    basketball_form_session = request.session.get('basketball_form', {})
    toque_form_session = request.session.get('toque_form', {})

    print(mens_form_session)

    event_costs = {
        'show_n_shine': 25,
        'poker_run': 5,
        'cruise_night': 0,
        'street_dance': 0,
    }

    event_total = sum(event_costs[key] for key, value in event_form_session.items() if value)

    merchandise_total = 0
    for quantity in mens_form_session.values():
        merchandise_total += 25 * (quantity or 0)
    for quantity in womens_form_session.values():
        merchandise_total += 25 * (quantity or 0)
    for quantity in basketball_form_session.values():
        merchandise_total += 20 * (quantity or 0)
    for quantity in toque_form_session.values():
        merchandise_total += 15 * (quantity or 0)


    paypal_dict = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "amount": event_total+merchandise_total,  # Example amount
        "item_name": "Item Name",
        "invoice": uuid.uuid4(),
        "currency_code":"CAD",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('payment_done')),
        "cancel_return": request.build_absolute_uri(reverse('payment_cancelled')),
    }


    form = PayPalPaymentsForm(initial=paypal_dict)

    # messages.info(request, 'Payment successful... Continue with google.')
    # return redirect('account_login')

    return render(request,'pages/payment.html',{
        'event_session' : request.session.get('events_form_data'),
        'mens_form_session':request.session.get('mens_tshirt_form'),
        'womens_form_session':request.session.get('womens_tshirt_form'),
        'basketball_form_session': request.session.get('basketball_form'),
        'toque_form_session':request.session.get('toque_form'),
        'total_price':event_total+merchandise_total,
        'form':form,
        'event_total':event_total,
        'merchandise_total':merchandise_total

    })



def payment_done(request):
    messages.info(request, 'Payment successful... Continue with google.')
    return redirect('account_login')


@login_required
def verify(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if created:
        profile_form_session = request.session.get('personal_form_data', {})
        event_form_session = request.session.get('events_form_data', {})
        vehicle_form_session = request.session.get('vechicle_form_data', {})
        mens_form_session = request.session.get('mens_tshirt_form', {})
        womens_form_session = request.session.get('womens_tshirt_form', {})
        basketball_form_session = request.session.get('basketball_form', {})
        toque_form_session = request.session.get('toque_form', {})

        profile.fname = profile_form_session.get('fname', '')
        profile.lname = profile_form_session.get('lname', '')
        profile.email = profile_form_session.get('email', '')
        profile.phone = profile_form_session.get('phone', '')
        profile.street = profile_form_session.get('street', '')
        profile.city = profile_form_session.get('city', '')
        profile.prov = profile_form_session.get('prov', '')
        profile.postal = profile_form_session.get('postal', '')

        profile.show_n_shine_participation = event_form_session.get('show_n_shine', False)
        profile.poker_run_participation = event_form_session.get('poker_run', False)
        profile.cruise_night_participation = event_form_session.get('cruise_night', False)
        profile.street_dance_participation = event_form_session.get('street_dance', False)

        profile.save()

        Vehicle.objects.create(
            profile=profile,
            year=vehicle_form_session.get('year', ''),
            make=vehicle_form_session.get('make', ''),
            model=vehicle_form_session.get('model', '')
        )

        for item, quantity in mens_form_session.items():
            if quantity and quantity > 0:
                _, _, size, color = item.split('_')
                item_type = "Men's T-Shirt"

                Merchandise.objects.create(
                    profile=profile,
                    item_type=item_type,
                    size=size,
                    color=color,
                    quantity=quantity
                )

        for item, quantity in womens_form_session.items():
            if quantity and quantity > 0:
                _, _, size, color = item.split('_')
                item_type = "Women's T-Shirt"

                Merchandise.objects.create(
                    profile=profile,
                    item_type=item_type,
                    size=size,
                    color=color,
                    quantity=quantity
                )


        for item, quantity in toque_form_session.items():
            if quantity and quantity > 0:
                _, _, color, _ = item.split('_')
                item_type = "Toque"

                Merchandise.objects.create(
                    profile=profile,
                    item_type=item_type,
                    size='N/A',
                    color=color,
                    quantity=quantity
                )

        for item, quantity in basketball_form_session.items():
            if quantity and quantity > 0:
                _, _, color, _, _ = item.split('_')
                item_type = "Basketball Cap"

                Merchandise.objects.create(
                    profile=profile,
                    item_type=item_type,
                    size='N/A',
                    color=color,
                    quantity=quantity
                )


    return redirect('home')


def payment_cancelled(request):
    return HttpResponse("Payment cancelled.")



def dashboard(request):
    return render(request,'profile/dashboard.html')




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
