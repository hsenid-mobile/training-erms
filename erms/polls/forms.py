__author__ = 'govinda'

from django import forms
from .models import InfoBasic
# from .models import CreateUser


class InfoBasicForm(forms.ModelForm):
    class Meta:
        model = InfoBasic
        fields = ['First_name', 'Last_name', 'Age', 'Email']


# class CreateUserForm(forms.ModelForm):
#     class Meta:
#         model = CreateUser
#         widgets = {
#             'Password': forms.PasswordInput(),
        # }
        # fields = ['Username', 'Password']
