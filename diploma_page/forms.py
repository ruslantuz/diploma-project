from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':_('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':_('Repeat password')})