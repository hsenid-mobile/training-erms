from django import forms
from django.contrib.admin import widgets
from .models import *


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['NIC', 'FName', 'LName', 'FullName', 'Email', 'DOB',
                  'AddressLine1', 'ContactNum',
                  'Post', 'FacebookProf',
                  'LinkedInProf', 'Department', 'Objective', 'SpecialNotes']


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['Time', 'Date', 'Venue', 'HOD', 'Vacancy', 'Department', 'InterviewType']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HOD_Review', 'HR_Review']


class InterviewForm2(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['Interviewers']
        exclude = ['Time', 'Date', 'Venue', 'HOD', 'Vacancy', 'Department', 'InterviewType','NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HOD_Review', 'HR_Review']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['Post', 'Field', 'Duration']
        exclude = ['Person']


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualifications
        fields = ['QName', 'subject']


class SubQualificationForm(forms.ModelForm):
    class Meta:
        model = SubQualification
        fields = ['QName', 'Result', 'Subject', 'SubResult']
        exclude = ['Person']


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
        fields = ['Post', 'DeptID', 'NoOfPossitions', 'NoOfIntDone', 'DateOfPublish', 'ClosingDate']


class HodReviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['HOD_Review']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HR_Review',
                   'Time', 'Date', 'Venue', 'HOD', 'Interviewers', 'Vacancy', 'Department', 'InterviewType']


class HodMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['MsgType', 'MsgTopic', 'MsgCont', 'MsgAcceptance', 'Sender', 'Reciever']


class LoginForm(forms.ModelForm):
    class Meta:
        model = LogMode
        fields = ['username', 'password', 'remember']

