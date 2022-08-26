from accounts.models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name','role','username','email','phone','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None