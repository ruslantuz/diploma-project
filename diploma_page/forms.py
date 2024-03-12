from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django import forms
from django.forms import ModelForm
from diploma_page.models import Orders

class AccountCreationForm(UserCreationForm):
    login = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':_('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':_('Repeat password')})


class OrderForm(ModelForm):
    order = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Orders
        fields = ["trip", "person_count", "check_in", "check_out"]