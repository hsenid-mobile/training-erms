from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = ['Post','AltPost','Field','Duration','YearStart','YearEnd','Company', 'Notes','Personal']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['NIC', 'FName', 'LName', 'FullName', 'DOB',
                  'AddressLine1', 'ContactNum', 'Objective', 'Interests',
                  'Email', 'FacebookProf', 'DateRecieved',
                  'PersonalHighlight', 'LinkedInProf', 'Objective'
                  ]
        exclude = ['InterviewNo']


class InterviewForm(forms.ModelForm):
    Time = forms.TimeField(widget=TimeInput())
    Date = forms.DateField(widget=DateInput())

    class Meta:
        model = Interview
        fields = ['Time', 'Date', 'Venue', 'InterviewType']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HOD_Review', 'HR_Review']


class InterviewForm2(forms.ModelForm):

    class Meta:
        model = Interview_Interviewer
        fields = ['Interviewer', 'Interview']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['Personal', 'Post', 'Field', 'Duration', 'Company', 'AltPost', 'YearStart', 'YearEnd', 'Notes']


class SelectStatusForm(forms.ModelForm):
    class Meta:
        model = Personal_Interview
        fields = ['Status']
        exclude = ['Personal', 'Interview']


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
        fields = ['NoOfPossitions', 'DateOfPublish', 'ClosingDate']
        exclude = ['done', 'NoOfIntDone', 'Post_Dept']


class HodReviewForm(forms.ModelForm):
    done = forms.BooleanField(
        label='Done',
        required=True,
        initial=False
    )

    class Meta:
        model = Interview
        fields = ['HOD_Review', 'done']
        exclude = ['NoOfPasses', 'NoOfFails', 'NoOfOnHolds', 'Interviewer_Review', 'HR_Review',
                   'Time', 'Date', 'Venue', 'HOD', 'Interviewers', 'Vacancy', 'Department', 'InterviewType']


class MessageForm(forms.ModelForm):
    class Meta:
       model = Messages
       fields = ('Recieve', 'MsgCont', 'MsgType')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField()


class SubForm(forms.ModelForm):
    class Meta:
        model = Post_Dept
        fields = ['Post', 'Dept']