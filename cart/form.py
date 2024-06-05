from django import forms
from cart.models import *


from django import forms

class PaymentForm(forms.Form):
    accnumber = forms.CharField(
        label='Card Number',
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'inputstyle',
            'placeholder': 'XXXX XXXX XXXX',
            'id': 'cardNumber',
            'maxlength': '12'
        })
    )
    card_holder = forms.CharField(
        label='Card Holder',
        widget=forms.TextInput(attrs={
            'class': 'inputstyle',
            'placeholder': 'NAME',
            'id': 'holderName'
        })
    )
    validity = forms.CharField(
        label='Valid Thru',
        max_length=5,
        widget=forms.TextInput(attrs={
            'class': 'inputstyle',
            'placeholder': 'MM/YY',
            'id': 'expiry',
            'maxlength': '5'
        })
    )
    cvv = forms.CharField(
        label='CVV',
        max_length=3,
        widget=forms.PasswordInput(attrs={
            'class': 'inputstyle',
            'placeholder': '***',
            'id': 'cvv',
            'maxlength': '3'
        })
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={
            'placeholder': 'Address'
        })
    )
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone'
        })
    )

