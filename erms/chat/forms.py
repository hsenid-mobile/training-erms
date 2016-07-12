from django import forms
from ermsapp.models import *


class MessageForm(forms.ModelForm):
    class Meta:
       model = Messages
       fields = ('Reciever', 'MsgCont')


class Evaluation_Form(forms.ModelForm):

    class Meta:
        model = Personal_Interview_viewer
        fields = ['Comment', 'Rate', 'Personal_Interview']
        exclude = ['Status']
