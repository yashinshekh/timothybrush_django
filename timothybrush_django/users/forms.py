# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'name', 'street_address', 'city', 'province_state', 'postal_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form labels or attributes if needed
        self.fields['email'].label = 'Email Address'
        self.fields['province_state'].widget.attrs.update({'class': 'form-select'})  # Example: Add a CSS class to the widget
        del self.fields['password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use. Please use a different one.')
        return email

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.username = user.email  # Ensure username and email are the same
    #     if commit:
    #         user.save()
    #     return user



from django import forms

# Personal Information Form (Step 1)
class PersonalInfoForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email_address = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    province_state = forms.CharField(max_length=100)
    postal_zip_code = forms.CharField(max_length=10)

# Vehicle Information Form (Step 2)
class VehicleInfoForm(forms.Form):
    year = forms.IntegerField(min_value=1900, max_value=2024)
    make = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)

# Events Form (Step 3)
class EventsForm(forms.Form):
    show_n_shine = forms.BooleanField(required=False, label='Show \'n Shine ($25)')
    poker_run = forms.BooleanField(required=False, label='Poker Run ($5)')
    cruise_night = forms.BooleanField(required=False, label='Cruise Night (Free)')
    street_dance = forms.BooleanField(required=False, label='Street Dance (Free)')

# Pre-ordering Prices Form (Step 4)
class PreOrderForm(forms.Form):
    t_shirts = forms.IntegerField(min_value=0, label='T-Shirts ($25 each)', required=False)
    toques = forms.IntegerField(min_value=0, label='Toques ($20 each)', required=False)
    baseball_caps = forms.IntegerField(min_value=0, label='Baseball Caps ($30 each)', required=False)
