from .models import Client

from django import forms

from django.forms.widgets import TextInput

# - Add a client
class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'location', 'formula', 'notes', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Client Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Client Phone Number'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Client Location'}),
            'formula': forms.Textarea(attrs={'placeholder': 'Enter Formula (optional)'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes (optional)'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
        }

# - Update a client
class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'location', 'formula', 'notes', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Client Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Client Phone Number'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Client Location'}),
            'formula': forms.Textarea(attrs={'placeholder': 'Enter Formula'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter Notes'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
        }
