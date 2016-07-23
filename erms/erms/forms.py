from django import forms
from ermsapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#user registration forms start#

class user_form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email',)


class profile_form(forms.ModelForm):
    UPhoto = forms.ImageField(label='Profile Picture')
    class Meta:
        model=Users
        exclude = ('User',)
#user registration forms end#ta



class DegreeType_Form(forms.ModelForm):
    class Meta:
        model = DegreeType
        exclude = ()


class Degree_PostForm(forms.ModelForm):
    class Meta:
        model = Degree_For_Post
        exclude = ('Post',)


class Qual_PostForm(forms.ModelForm):
    class Meta:
        model = Qual_For_Post
        exclude = ('Post',)


class Exp_PostForm(forms.ModelForm):
    class Meta:
        model = Exp_Post
        exclude = ('Post',)

class SubQual_PostForm(forms.ModelForm):
    class Meta:
        model = subQul_Post
        exclude = ('Post',)


class PostForm(forms.ModelForm):
    #InterviewType = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple) #queryset=InterviewType.objects.all())
    class Meta:
        model = Post
        fields = ('Post','NoOfInterviews','Field')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields = ('DeptName',)


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post_Dept
        fields = ('Dept',)
        exclude = ('Post',)