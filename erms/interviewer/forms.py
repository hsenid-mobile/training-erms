from django import forms
from ermsapp.models import *


class Evaluation_Form(forms.ModelForm):
    class Meta:
        model = Personal_Interview_viewer
        fields = ('Comment', 'Rate')

class Review_Form(forms.ModelForm):

    class Meta:
        model = Interview
        fields = ('Interviewer_Review',)

