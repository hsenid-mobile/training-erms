from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['NIC', 'FName', 'LName', 'FullName', 'DOB',
                  'AddressLine1', 'ContactNum', 'Objective', 'Interests',
                  'Email', 'DeptPost', 'FacebookProf', 'DateRecieved',
                  'PersonalHighlight', 'LinkedInProf', 'Objective'
                  ]


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['Time', 'Date', 'Venue', 'HOD', 'Vacancy', 'Department', 'InterviewType']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HOD_Review', 'HR_Review']


class InterviewForm2(forms.ModelForm):
    class Meta:
        model = Interview_Interviewer
        fields = ['Interviewer']
        exclude = ['Interview']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['Post', 'Field', 'Duration', 'Company',
                  'AltPost', 'YearStart', 'YearEnd', 'Notes']
        exclude = ['Personal']


class PersonInterForm(forms.ModelForm):
    class Meta:
        model = Personal_Interview
        fields = ['Personal', 'Interview']


class SubQualificationForm(forms.ModelForm):
    class Meta:
        model = SubQualification
        fields = ['QName', 'Subject', 'Result', 'SubResult', 'QType', 'SpecialNotes']
        exclude = ['Personal']


class SpecializedAreaForm(forms.ModelForm):
    class Meta:
        model = SpecializedArea
        fields = ['SpecializedArea']


class VacancyForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(VacancyForm, self).__init__(*args, **kwargs)
    #     self.fields['DateOfPublish'].widget = widgets.AdminDateWidget()
    #     self.fields['ClosingDate'].widget = widgets.AdminTimeWidget()

    class Meta:
        model = Vacancy
        fields = ['Post_Dept', 'NoOfPossitions', 'NoOfIntDone', 'DateOfPublish', 'ClosingDate']


class HodReviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['HOD_Review']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HR_Review',
                   'Time', 'Date', 'Venue', 'HOD', 'Interviewers', 'Vacancy', 'Department', 'InterviewType']


class HodMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['MsgType', 'MsgCont', 'MsgAcceptance', 'Send', 'Recieve']
        exclude = ['SentDate', 'SentTime', 'RecievedDate', 'RecievedTime']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField()


class SubForm(forms.ModelForm):
    class Meta:
        model = Post_Dept
        fields = ['Post', 'Dept']