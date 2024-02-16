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
        disabled=True,
        initial=True,
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

class MenstshirtForm(forms.Form):
    SIZES = ['Small', 'Medium', 'Large', 'X-Large', '2X-Large', '3X-Large']
    COLORS = ['Black', 'White', 'Grey']

    def __init__(self, *args, **kwargs):
        super(MenstshirtForm, self).__init__(*args, **kwargs)

        for size in self.SIZES:
            for color in self.COLORS:
                # Only creating a quantity field for each T-shirt option
                field_name = f'quantity_{size}_{color}'
                self.fields[field_name] = forms.IntegerField(
                    label=f'{size} {color}',
                    required=False, min_value=0, initial=0,max_value=10,
                    widget=forms.NumberInput(attrs={'class': 'quantity-input'}))


    def clean(self):
        cleaned_data = super().clean()

        for size in self.SIZES:
            for color in self.COLORS:
                shirt_key = f'{size}_{color}'
                quantity_key = f'quantity_{size}_{color}'

                shirt_selected = cleaned_data.get(shirt_key)
                quantity = cleaned_data.get(quantity_key, 0)

                # If a shirt is selected but quantity is 0, or vice versa, raise a validation error
                if shirt_selected and quantity <= 0:
                    self.add_error(quantity_key, f'Please enter a valid quantity for {size} {color} T-Shirt.')

                if not shirt_selected and quantity > 0:
                    self.add_error(shirt_key, f'Please select the {size} {color} T-Shirt before specifying a quantity.')

        return cleaned_data



class WomenstshirtForm(forms.Form):
    SIZES = ['Small', 'Medium', 'Large', 'X-Large', '2X-Large']
    COLORS = ['Black', 'White', 'Grey']

    def __init__(self, *args, **kwargs):
        super(WomenstshirtForm, self).__init__(*args, **kwargs)

        for size in self.SIZES:
            for color in self.COLORS:
                # Only creating a quantity field for each T-shirt option
                field_name = f'quantity_{size}_{color}'
                self.fields[field_name] = forms.IntegerField(
                    label=f'{size} {color}',
                    required=False, min_value=0, initial=0,max_value=10,
                    widget=forms.NumberInput(attrs={'class': 'quantity-input'}))


    def clean(self):
        cleaned_data = super().clean()

        for size in self.SIZES:
            for color in self.COLORS:
                shirt_key = f'{size}_{color}'
                quantity_key = f'quantity_{size}_{color}'

                shirt_selected = cleaned_data.get(shirt_key)
                quantity = cleaned_data.get(quantity_key, 0)

                # If a shirt is selected but quantity is 0, or vice versa, raise a validation error
                if shirt_selected and quantity <= 0:
                    self.add_error(quantity_key, f'Please enter a valid quantity for {size} {color} T-Shirt.')

                if not shirt_selected and quantity > 0:
                    self.add_error(shirt_key, f'Please select the {size} {color} T-Shirt before specifying a quantity.')

        return cleaned_data



class PaymentForm(forms.Form):
    confirm_payment = forms.BooleanField(required=True, label="Yes... I confirm that I have read and understand all terms and conditions above. *	")


    def clean(self):
        if not self.confirm_payment:
            raise forms.ValidationError("You must confirm the payment to proceed.")

        return self.cleaned_data


