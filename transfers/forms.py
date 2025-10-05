from django import forms
from .models import dbc

class TransferForm(forms.Form):
    sender = forms.CharField(max_length=14)
    receiver = forms.CharField(max_length=14)
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    tpin = forms.CharField(max_length=4, widget=forms.PasswordInput)
    description = forms.CharField(max_length=255, required=False)
