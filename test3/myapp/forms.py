from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['NIC', 'FName', 'LName', 'FullName', 'DOB',
                  'AddressLine1', 'ContactNum', 'Objective', 'Interests',
                  'Email', 'DeptPost', 'FacebookProf', 'DateRecieved',
                  'PersonalHighlight', 'LinkedInProf', 'Objective'
                  ]
        exclude = ['InterviewNo']


class InterviewForm(forms.ModelForm):
    Time = forms.TimeField(widget=TimeInput())
    Date = forms.DateField(widget=DateInput())

    class Meta:
        model = Interview
        fields = ['Time', 'Date', 'Venue', 'InterviewType', 'Post']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HOD_Review', 'HR_Review']


class InterReviewForm(forms.ModelForm):

    class Meta:
        model = Interview
        fields = ['HOD_Review']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'Time', 'Date', 'Venue', 'HOD', 'Department', 'InterviewType', 'HR_Review', 'InterviewNo', 'Vacancy']


class InterviewForm2(forms.ModelForm):

    class Meta:
        model = Interview_Interviewer
        fields = ['Interviewer', 'Interview']


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
    DateOfPublish = forms.DateField(widget=DateInput())
    ClosingDate = forms.DateField(widget=DateInput())

    class Meta:
        model = Vacancy
        fields = ['Post_Dept', 'NoOfPossitions', 'NoOfIntDone', 'DateOfPublish', 'ClosingDate']
        exclude = ['done']


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