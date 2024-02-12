from django import forms

class PersonalInfo(forms.Form):
    fname = forms.CharField(label='First Name',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lname = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number','type':'tel'}))
    street = forms.CharField(label='Street Address', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Street Address'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    prov = forms.CharField(label='Province/State', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Province / State'}))
    postal = forms.CharField(label='Postal/Zip Code', max_length=10, widget=forms.NumberInput(attrs={'placeholder': 'Postal/Zip Code'}))


class VechicleInfo(forms.Form):
    CAR_MAKE_CHOICES = [
        ("", "-- Select Make --"),
        ("AC", "AC"),
        ("Abarth", "Abarth"),
        ("Acura", "Acura"),
        ("Volvo", "Volvo"),
        ("W Motors", "W Motors"),
        ("ZAZ", "ZAZ"),
        ("Zagato", "Zagato"),
        ("Zil", "Zil"),
    ]

    year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Year'}), label="Year", required=True)
    make = forms.ChoiceField(choices=CAR_MAKE_CHOICES, label="Make", required=True)
    model = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Model'}), label="Model", required=True)



class EventInfo(forms.Form):
    show = forms.BooleanField(
        label="Show 'n Shine ($25.00)",
        required=False,
        disabled=True,  # This field is disabled and always checked by default as per your HTML
        initial=True,  # Set initial value to True since it's checked by default
        widget=forms.CheckboxInput(attrs={'class': ''})
    )
    poker = forms.BooleanField(
        label="Poker Run ($5.00)",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': ''})
    )
    cruise_night = forms.BooleanField(
        label="Cruise Night (Free)",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': ''})
    )
    dance = forms.BooleanField(
        label="Street Dance (Free)",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': ''})
    )


class Memorabilia(forms.Form):
    name = forms.CharField(label="Name")
