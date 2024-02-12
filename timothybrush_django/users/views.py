from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render, redirect

from .forms import PersonalInfo,VechicleInfo

User = get_user_model()


def home(request):
    if request.method == 'POST':
        personal_form = PersonalInfo(request.POST)
        if personal_form.is_valid():
            request.session['personal_form_data'] = personal_form.cleaned_data
            v_form = VechicleInfo()
            next_step_html = render_to_string('pages/vechicle_form.html', {'vechicle_form': v_form}, request=request)
            return HttpResponse(next_step_html)
    else:
        session_form_data = request.session.get('personal_form_data')
        if session_form_data:
            personal_form = PersonalInfo(initial=session_form_data)
        else:
            personal_form = PersonalInfo()

    return render(request, 'pages/home.html', {'personal_form': personal_form})


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
