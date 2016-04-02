from django import forms
from .models import LogMode

class LogForm(forms.Form):
    class meta:
        model = LogMode
        fields = ['Username', 'Password']