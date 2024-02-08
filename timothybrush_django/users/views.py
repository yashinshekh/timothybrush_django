from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

# User = get_user_model()

from django.contrib.auth import login
from django.shortcuts import render,redirect
from .models import User
# from .forms import SignupForm
from .forms import PersonalInfoForm, VehicleInfoForm, EventsForm, PreOrderForm
from formtools.wizard.views import SessionWizardView

# def home(request):
#     return render(request,'pages/home.html')

class MultiStepFormWizard(SessionWizardView):
    template_name = "pages/home.html"
    form_list = [PersonalInfoForm, VehicleInfoForm, EventsForm, PreOrderForm]

    def done(self, form_list, **kwargs):
        # Process the collected form data
        form_data = [form.cleaned_data for form in form_list]

        # Example: Do something with the form_data here (e.g., save to a database, send an email, etc.)

        return render(self.request, 'pages/form_completed.html', {'form_data': form_data})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {'form': form})


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
