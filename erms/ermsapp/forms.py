from django import forms
from .models import *
from django.contrib.auth.models import User
from bootstrap3_datetime.widgets import DateTimePicker


class DateInput(forms.DateInput):
    input_type = 'date'


#personal
class DEO_Entry_PersonalForm(forms.ModelForm):
    PImage = forms.ImageField(label='Personal Image',help_text="Upload Profile Image")
    CVImage = forms.ImageField(label='CV Image',help_text="Upload CV Image",required=False)
    FName = forms.CharField(label = "First Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter First Name",required=True)
    LName = forms.CharField(label = "Last Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter Last Name")
    FullName = forms.CharField(label = "Full Name",widget=forms.TextInput(attrs={'size':50}),help_text="Enter Full Name e.g: John Fitzgerald Kennedy")
    ContactNum = forms.CharField(label="Contact Number",widget=forms.TextInput(attrs={'size':10}),help_text="e.g: 071xxxxxxx")
    DOB = forms.DateField(label="Date Of Birth",widget=DateInput())
    Email = forms.EmailField(help_text="e.g: someone@somemail.com")
    FacebookProf = forms.CharField(label="Facebook Name",widget=forms.TextInput(attrs={'size':50}))
    LinkedInProf = forms.CharField(label="LinkedIn Name",widget=forms.TextInput(attrs={'size':50}))
    AddressLine1 = forms.CharField(label="Address Line 1",widget=forms.TextInput(attrs={'size':50}))
    AddressLine2 = forms.CharField(label="Address Line 2",widget=forms.TextInput(attrs={'size':50}))
    AddressLine3 = forms.CharField(label="Address Line 3",widget=forms.TextInput(attrs={'size':50}))
    Nationality = forms.CharField(label="Nationality",widget=forms.TextInput(attrs={'size':50}))
    DateRecieved = forms.DateField(label='Date Recieved Cv',widget=DateInput())

    class Meta:
        model = Personal
        exclude = ('Dept_Post','RecruitedPost',)#('FName','LName','FullName','NIC','Nationality','DOB','AddressLine1','AddressLine2','AddressLine3','AddressLine4','ContactNum','Email','FacebookProf','LinkedInProf','PImage','CVPDF','Objective','SpecialNotes')
        widgets = {
                  'PersonalHighlight': forms.Textarea(attrs={'rows':6, 'cols':50}),
                  'Objective': forms.Textarea(attrs={'rows':6, 'cols':50}),
                  'Interests' : forms.Textarea(attrs={'rows':4})
                 }

#personal


class DEO_Entry_OoAQualification(forms.ModelForm):

    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult",)


#Other Qualification
class DEO_Entry_QualificationForm(forms.ModelForm):
    class Meta:
        model = SubQualification
        exclude = ("Subject", "SubResult")


class DEO_Entry_QualResultForm(forms.ModelForm):
    NoOfA = forms.IntegerField(label="Number of As")
    NoOfB = forms.IntegerField(label="Number of Bs")
    NoOfC = forms.IntegerField(label="Number of Cs")
    class Meta:
        model = QualResult
        exclude = ('Personal','QName')


class DEO_Entry_SubQualificationForm(forms.ModelForm):
    Subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'size':50}))
    SubResult = forms.CharField(label='Result',widget=forms.TextInput(attrs={'size':5}))

    class Meta:
        model = SubQualification
        fields = ("Subject","SubResult")


class DEO_DegreeChoiceForm(forms.ModelForm):

    class Meta:
        model = Degree
        fields =('University','DegreeType','DegreeField')


class DEO_Entry_DegreeForm(forms.ModelForm):
    YearStart = forms.IntegerField(label='Enrolled Year')
    YearEnd = forms.IntegerField(label='Leaving Year')
    class Meta:
        model = Personal_Degree
        fields =('YearStart','YearEnd','Class','SpecialNotes')


class DEO_Entry_Skill1(forms.ModelForm):
    class Meta:
        model = Skill
        fields =('Skill','Description')


class DEO_Entry_ExtraForm1(forms.ModelForm):

    class Meta:
        model = Extracurricular
        fields =('Extracurricular','Description')


class DEO_Entry_SportForm1(forms.ModelForm):
    Sports = forms.Textarea()
    class Meta:
        model = Sports
        fields =('Sports','Description')


class DEO_Entry_ExperienceForm(forms.ModelForm):
    YearStart = forms.IntegerField(label='Starting Year')
    YearEnd = forms.IntegerField(label='Leaving Year')
    AltPost = forms.CharField(label = "Alternative Post", help_text="If the Post is not defiened above enter your post")
    class Meta:
        model = Experience
        exclude = ('Personal',)
        widgets = {
                  'Notes': forms.Textarea(attrs={'rows':6, 'cols':100}),
                }


class DEO_Enrety_SpecialAchievements(forms.ModelForm):
    Heading_1 = forms.CharField(label="Main Heading")
    Heading_2 = forms.CharField(label="Sub Heading")
    class Meta:
        model = SpecialAchievements
        exclude = ("Person",)



class DEO_EntryForm(forms.Form):
    NIC = forms.CharField(widget=forms.TextInput(attrs={'size':50}),help_text="Enter Person's NIC number")



