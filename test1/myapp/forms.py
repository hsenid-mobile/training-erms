from django.forms import ModelForm
from django import forms
from .models import Person, Log_Mode

class Log_Form(ModelForm):
    class meta:
        model = Log_Mode
        fields = ['Username', 'Password']

# class cv_form(forms.Form):
#     class meta:

class Interview_Form(forms.ModelForm):
    class meta:
        model = Person
        fields = ['NIC', 'FName', 'LName','FullName','Email']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Log_Mode
        fields = ['username', 'password', 'remember']

