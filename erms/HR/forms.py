from django import forms
from ermsapp.models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('Reciever', 'MsgCont')


class NewPost1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Post', 'Field', 'NoOfInterviews', 'InterviewType']


class PostDept(forms.ModelForm):
    class Meta:
        model = Post_Dept
        fields = ['Post', 'Dept']


class DegPost(forms.ModelForm):
    class Meta:
        model = Degree_For_Post
        fields = ['Post', 'Degree']


class SubQualif(forms.ModelForm):
    class Meta:
        model = subQul_Post
        fields = ['Post', 'QName', 'Subject', 'SubResult']


class ProfQualif(forms.ModelForm):
    class Meta:
        model = Exp_Post
        fields = ['Post', 'ExPost', 'Duration']


class CvForDept(forms.ModelForm):
    class Meta:
        model = Personal_Post_Dept
        fields = ['DeptPost']
