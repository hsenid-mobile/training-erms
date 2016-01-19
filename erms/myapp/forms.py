from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import PersonInfo, Education, CreatUser

#for Login page
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=None) #widget=forms.widget.TextInput
    password = forms.CharField(label="Password", required=None ) #widget=forms.widget.PasswordInput
    remember = forms.BooleanField(label="Remember Me?")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login', css_class='btn-primary'))
    class Meta:
        fields = ['username', 'password']


#Registration Form
# class RegistrationForm(forms.ModelForm):
#       class Meta:
#         model = CreatUser
#         password2 = password2 = forms.CharField(label="password (again)") #widget=forms.widget.PasswordInput,
#         fields = ['username', 'password', 'password2']
#
#       def clean(self):
#         cleaned_data = super(RegistrationForm, self).clean()
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
#         return self.cleaned_data

#for deo page
class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['firstName','lastName','email','address','age','gender','telephone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.spit('.')
        if not extension == "com" :
            raise forms.ValidationError("Enter correct type of email")

    def clean_age(self):
        age = self.clean_data.get('age')
        if not age > 0 :
            raise forms.ValidationError("Enter possible age")

class EducationForm(forms.Form):
    class Met:
        model = Education
        fields = ["university", "degree", "average_gpa", "from_year", "to_year",  "description",
                  "secondary_education", "gca_al_stream", "gca_ol_stream"]

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ['user']