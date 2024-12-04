from .models import Client

from django import forms

from django.forms.widgets import TextInput

# - Add a client
class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'location', 'formula', 'notes', 'price']

# - Update a client
class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'location', 'formula', 'notes', 'price']
