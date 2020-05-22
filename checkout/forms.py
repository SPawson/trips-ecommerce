from django import forms
from .models import OrderInformation, OrderLineItem

#Code snippets taken from Code Institute's Ecommerce lessons

class OrderForm(forms.ModelForm):
    """ The form will collect user information for billing"""

    class Meta: 
        model = OrderInformation
        fields = [
            'firstname',
            'lastname',
            'phone_number',
            'address1',
            'address2',
            'town_or_city',
            'postcode',
            'county',
            'country',
        ]

class MakePaymentForm(forms.Form):
    """Form which allows payments to be made"""
    MONTH_CHOICES = [(i, i) for i in range(1,12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput) #Hidden from the user