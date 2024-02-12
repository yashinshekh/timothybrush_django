from django import forms

class PersonalForm(forms.Form):
    fname = forms.CharField(label='First Name',max_length=100,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lname = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number','type':'tel'}))
    street = forms.CharField(label='Street Address', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Street Address'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    prov = forms.CharField(label='Province/State', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Province / State'}))
    postal = forms.CharField(label='Postal/Zip Code', max_length=10, widget=forms.NumberInput(attrs={'placeholder': 'Postal/Zip Code'}))


class VechicleForm(forms.Form):
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



class EventForm(forms.Form):
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


class MemorabiliaForm(forms.Form):
    tshirt = forms.BooleanField(label='T-Shirt ($25.00 each)', required=False)
    toque = forms.BooleanField(label='Toque ($20.00 each)', required=False)
    cap = forms.BooleanField(label='Baseball Cap ($30.00 each)', required=False)


class PaymentForm(forms.Form):
    confirm_payment = forms.BooleanField(required=True, label="I confirm my payment.")


    def clean(self):
        if not self.confirm_payment:
            raise forms.ValidationError("You must confirm the payment to proceed.")

        return self.cleaned_data


