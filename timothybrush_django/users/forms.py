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

