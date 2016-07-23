# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def Person_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Person_{0}/{1}'.format(instance.Person.id, filename)


def User_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Person_{0}/{1}'.format(instance.User.id, filename)


class Person(models.Model):
    NIC = models.CharField(unique=True,max_length=12)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    FullName = models.CharField(max_length=100)
    DOB = models.DateField()
    Nationality = models.CharField(max_length=20)
    AddressLine1 = models.CharField(max_length=100)
    AddressLine2 = models.CharField(max_length=100)
    AddressLine3 = models.CharField(max_length=100)
    AddressLine4 = models.CharField(max_length=100, null=True,blank=True)
    ContactNum = models.CharField(max_length=12)
    Email = models.EmailField()
    FacebookProf = models.CharField(max_length=100,null=True,blank=True)
    LinkedInProf = models.CharField(max_length=100,null=True,blank=True)
    PImage = models.ImageField(upload_to= Person_directory_path,null=True)
    Objective = models.TextField()
    CVPDF = models.ImageField(upload_to=Person_directory_path)
    SpecialNotes = models.TextField(blank=True,null=True)
    Department = models.ManyToManyField("Department")
    Post = models.ManyToManyField("Post")
    Degree = models.ManyToManyField("Degree",through="Person_Degree",null=True)
    Interview = models.ManyToManyField("Interview",through='Person_Interview',null=True)

    def __str__(self):
        return self.NIC, self.FName, self.LName, self.FullName, self.Email


class Skill(models.Model):
    Skill = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Sports(models.Model):
    Sports = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Extracurricular(models.Model):
    Extracurricular = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Person_Interview(models.Model):
    Person = models.ForeignKey(Person)
    Interview = models.ForeignKey("Interview")
    Interviewers =models.ManyToManyField("Interviewers",through='Person_Interview_viewer')


class Person_Interview_viewer(models.Model):
    Interviewers = models.ForeignKey('Interviewers')
    Person_Interview = models.ForeignKey(Person_Interview)
    Comment = models.TextField()
    Rate = models.PositiveSmallIntegerField()
    Status = models.ForeignKey("CV_Status")


class CV_Status(models.Model):
    Status = models.CharField(max_length=10)

    def __str__(self):
        return self.Status


class Department(models.Model):
    DeptName = models.CharField(max_length=30)

    def __str__(self):
        return self.DeptName


class InterviewType(models.Model):
    InterviewType = models.CharField(max_length=30)

    def __str__(self):
        return self.InterviewType


class Post(models.Model):
    Post = models.CharField(max_length=100)
    NoOfInterviews = models.PositiveIntegerField()
    InterviewType = models.ManyToManyField(InterviewType)

    def __str__(self):
        return self.Post


class Degree(models.Model):
    University = models.CharField(max_length=30)
    Degree = models.CharField(max_length=30)
    DegreeType = models.ForeignKey("DegreeType")

    def __str__(self):
        return self.University,self.Degree,self.DegreeType


class DegreeType(models.Model):
    Type = models.CharField(max_length=10)
    def __str__(self):
        return self.Type


class Person_Degree(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    Year = models.DateField()
    SpecialNotes = models.TextField(null=True)
    GPA = models.FloatField()


class UserRole(models.Model):
    Role = models.CharField(max_length=15)


class UserRole(models.Model):
    Role = models.CharField(max_length=15)

    def __str__(self):
        return self.Role


class Users(models.Model):
    User = models.OneToOneField(User)
    FullName = models.CharField(max_length=100)
    Post = models.ForeignKey(Post)
    UPhoto = models.ImageField(upload_to=User_directory_path)
    Department = models.ForeignKey(Department)
    UserRole = models.ForeignKey(UserRole)


    def __str__(self):
        return self.UName


class Interviewers(Users):
    NoOfInts = models.PositiveIntegerField(null=True,blank=True)
    SpecializedArea = models.ManyToManyField('SpecializedArea')
    Interview = models.ManyToManyField("Interview")


class SpecializedArea(models.Model):
    SpecializedArea = models.CharField(max_length=100)


class Interview(models.Model):
    Time = models.TimeField()
    Date = models.DateField()
    Venue = models.ForeignKey('Venue')
    HOD = models.ForeignKey(Users)
    Post = models.ForeignKey(Post)
    Vacancy = models.ForeignKey('Vacancy')
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    InterviewType = models.ForeignKey(InterviewType, on_delete=models.CASCADE)


class InterviewHistory(models.Model):
    Interviewer_Review = models.TextField(blank=True,null=True)
    HOD_Review = models.TextField(blank=True,null=True)
    HR_Review = models.TextField(blank=True,null=True)
    NoOfPasses = models.PositiveIntegerField()
    NoOfFails = models.PositiveIntegerField()
    NoOfOnHolds = models.PositiveIntegerField()


class Venue(models.Model):
    HallName = models.CharField(max_length=40)

    def __str__(self):
        return self.HallName


class Vacancy(models.Model):
    DateOfPublish = models.DateField()
    ClosingDate = models.DateField()
    NoOfIntDone = models.IntegerField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE)


class Experience(models.Model):
    Post = models.CharField(max_length=100)
    Field = models.CharField(max_length=100)
    Duration = models.FloatField(max_length=2.2)
    Notes = models.TextField()
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.Post,self.Type


class Qualifications(models.Model):
    QName = models.CharField(max_length=100)
    Result = models.CharField(max_length=20)
    person = models.ForeignKey("Person")

    def __str__(self):
        return self.QName,self.Result


class SubQualification(models.Model):
    QName = models.CharField(max_length=100)
    Subject = models.CharField(max_length=200)
    SubResult = models.CharField(max_length=4)
    person = models.ForeignKey("Person")

    def __str__(self):
        return self.Subject,self.SubResult



class Log_Mode(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    remember = models.BooleanField()

    def __str__(self):
        return self.username,self.password,self.remember