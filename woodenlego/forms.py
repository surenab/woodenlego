from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES=[('0','No'),
         ('1','Yes')]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    telephone = forms.CharField(max_length=40, required=False,help_text='Optional.')
    newsletter = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,initial='1')
    agree = forms.BooleanField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telephone' ,'password1', 'password2', 'newsletter', 'agree')