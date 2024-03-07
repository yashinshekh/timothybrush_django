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
    show_n_shine = forms.BooleanField(label="Show 'n Shine ($25.00)", required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': ''}))
    poker_run = forms.BooleanField(label="Poker Run ($5.00)", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))
    cruise_night = forms.BooleanField(label="Cruise Night (Free)", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))
    street_dance = forms.BooleanField(label="Street Dance (Free)", required=False, widget=forms.CheckboxInput(attrs={'class': ''}))


class MenstshirtForm(forms.Form):
    SIZES = ['Small', 'Medium', 'Large', 'X-Large', '2X-Large', '3X-Large']
    COLORS = ['Black', 'White', 'Grey']

    def __init__(self, *args, **kwargs):
        super(MenstshirtForm, self).__init__(*args, **kwargs)

        for size in self.SIZES:
            for color in self.COLORS:
                field_name = f'men_quantity_{size}_{color}'
                self.fields[field_name] = forms.IntegerField(
                    label=f'{size} {color}',
                    required=False, min_value=0,max_value=10,
                    widget=forms.NumberInput(attrs={
                        'class': 'quantity-input h-2 p-1',
                    }))



class WomenstshirtForm(forms.Form):
    SIZES = ['Small', 'Medium', 'Large', 'X-Large', '2X-Large']
    COLORS = ['Black', 'White', 'Grey']

    def __init__(self, *args, **kwargs):
        super(WomenstshirtForm, self).__init__(*args, **kwargs)

        for size in self.SIZES:
            for color in self.COLORS:
                field_name = f'women_quantity_{size}_{color}'
                self.fields[field_name] = forms.IntegerField(
                    label=f'{size} {color}',
                    required=False, min_value=0, initial=0,max_value=10,
                    widget=forms.NumberInput(attrs={'class': 'quantity-input'}))



class ToquesForm(forms.Form):
    COLORS = [
        'Black Toque','Forest Green Toque','Navy Toque', 'Charcoal Toque', 'Light Grey Toque'
    ]

    def __init__(self,*args,**kwargs):
        super(ToquesForm,self).__init__(*args,**kwargs)
        for color in self.COLORS:
            field_name = f'toque_quantity_{color.replace(" ", "_")}'
            self.fields[field_name] = forms.IntegerField(
                label=color,
                required=False, min_value=0, max_value=10,
                widget=forms.NumberInput(attrs={'class': 'quantity-input'}))


class BasketballForm(forms.Form):
    COLORS = [
        'Black Ball Cap','Beige Ball Cap'
    ]

    def __init__(self,*args,**kwargs):
        super(BasketballForm,self).__init__(*args,**kwargs)
        for color in self.COLORS:
            field_name = f'basketball_quantity_{color.replace(" ", "_")}'
            self.fields[field_name] = forms.IntegerField(
                label=color,
                required=False, min_value=0, max_value=10,
                widget=forms.NumberInput(attrs={'class': 'quantity-input'}))




class TOSForm(forms.Form):
    confirm_payment = forms.BooleanField(required=True, label="Yes... I confirm that I have read and understand all terms and conditions above. *	")


    def clean(self):
        cleaned_data = super().clean()  # Call the base class first
        confirm_payment = cleaned_data.get('confirm_payment')  # Use .get to avoid KeyError if not present

        if not confirm_payment:
            raise forms.ValidationError("You must confirm the payment to proceed.")

        return cleaned_data


