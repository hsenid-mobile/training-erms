from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def Person_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Uploadfiles/Person_%s/%s' % (instance.NIC, filename)


def User_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Uploadfiles/User_%s/%s' % (instance.User.id, filename)


class Personal(models.Model):
    NIC = models.CharField(unique=True,max_length=12)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    FullName = models.CharField(max_length=100)
    DOB = models.DateField(null=True)
    DateRecieved = models.DateField()
    Nationality = models.CharField(max_length=20)
    AddressLine1 = models.CharField(max_length=100)
    AddressLine2 = models.CharField(max_length=100)
    AddressLine3 = models.CharField(max_length=100)
    ContactNum = models.CharField(max_length=12)
    Email = models.EmailField(null=True, blank=True)
    FacebookProf = models.CharField(max_length=100, null=True, blank=True)
    LinkedInProf = models.CharField(max_length=100, null=True, blank=True)
    PImage = models.FileField(upload_to=Person_directory_path, null=True, blank=True)
    Interests = models.TextField(null=True, blank=True)
    Objective = models.TextField(null=True, blank=True)
    CVImage = models.FileField(upload_to=Person_directory_path, null=True, blank=True)
    PersonalHighlight = models.TextField(blank=True, null=True)
    # DeptPost = models.ForeignKey("Post_Dept")
    RecuritedPost = models.ForeignKey("Post") #NEWLY ADDED FIELD

    def __str__(self):
        return self.FullName


class Personal_Post_Dept(models.Model): # add by hr
    Personal = models.ForeignKey(Personal)
    Post_Dept = models.ForeignKey('Post_Dept')

    def __str__(self):
        return u'{}'.format(self.Personal)


class Skill(models.Model):
    Skill = models.CharField(max_length=100)
    Description  = models.TextField()
    person = models.ForeignKey("Personal", on_delete=models.CASCADE)


class Sports(models.Model):
    Sports = models.CharField(max_length=100)
    Description = models.TextField()
    person = models.ForeignKey("Personal", on_delete=models.CASCADE)


class Extracurricular(models.Model):
    Extracurricular = models.CharField(max_length=100)
    Description = models.TextField()
    person = models.ForeignKey("Personal", on_delete=models.CASCADE)


class SpecialAchievements(models.Model):
    Person = models.ForeignKey(Personal)
    Heading_1 = models.CharField(max_length=100)
    Heading_2 = models.CharField(max_length=100)
    Notes = models.TextField()


class Personal_Interview(models.Model):
    Personal = models.ForeignKey(Personal)
    Interview = models.ForeignKey("Interview")
    Status = models.ForeignKey("CV_Status", null=True)

    def __str__(self):
        return u'{}'.format(self.Personal)


class Personal_Interview_viewer(models.Model):
    Interviewer = models.ForeignKey(User)
    Personal_Interview = models.ForeignKey(Personal_Interview)
    Comment = models.TextField()
    Rate = models.PositiveSmallIntegerField()

    def __str__(self):
        return u'{}'.format(self.Personal_Interview)


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
    Field = models.CharField(max_length=100,null=True,blank=True)
    NoOfInterviews = models.PositiveIntegerField()
    InterviewType = models.ManyToManyField(InterviewType)

    def __str__(self):
        return self.Post


class Post_Dept(models.Model):
    Post = models.ForeignKey('Post')
    Dept = models.ForeignKey('Department')

    def __str__(self):
        return u'{}'.format(self.Post)


class University(models.Model):
    university = models.CharField(max_length=100)

    def __str__(self):
        return self.university


class Degree(models.Model):
    University = models.ForeignKey(University)
    DegreeType = models.ForeignKey("DegreeType") #Phd ,BSc ,MSc
    DegreeField = models.ForeignKey("DegreeField") #Egineering,Bio Science,Arts,IT

    def __str__(self):
        return self.Degree, self.University


class DegreeField(models.Model):
    Field = models.CharField(max_length=100)

    def __str__(self):
        return self.Field


class DegreeType(models.Model):
    Type = models.CharField(max_length=10)
    HierachyNumber = models.IntegerField()

    def __str__(self):
        return self.Type


class Personal_Degree(models.Model):
    Personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    Degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    YearStart = models.IntegerField()
    YearEnd = models.IntegerField()
    SpecialNotes = models.TextField(null=True)
    Class = models.ForeignKey('Degree_class',null=True,blank=True)


class Degree_class(models.Model):
    Class = models.CharField(max_length=20)

    def __str__(self):
        return self.Class


class UserRole(models.Model):
    Role = models.CharField(max_length=15)

    def __str__(self):
        return self.Role


class Degree_For_Post(models.Model):
    Degree = models.ForeignKey(Degree)
    Post = models.ForeignKey(Post)


class Users(models.Model):
    User = models.OneToOneField(User)
    FullName = models.CharField(max_length=100)
    Post = models.ForeignKey(Post)
    UPhoto = models.FileField(upload_to=User_directory_path,null = True,blank=True)
    Department = models.ForeignKey(Department)
    UserRole = models.ForeignKey(UserRole)

    def __str__(self):
        return u'{}'.format(self.User)


class SpecializedArea(models.Model):
    interviewer = models.ForeignKey(User)
    SpecializedArea = models.CharField(max_length=100)


class Interview(models.Model):
    Time = models.TimeField()
    Date = models.DateField()
    Venue = models.ForeignKey('Venue')
    HOD = models.ForeignKey(User)
    Vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    InterviewType = models.ForeignKey(InterviewType, on_delete=models.CASCADE)
    Interviewer_Review = models.TextField(blank=True, null=True)
    HOD_Review = models.TextField(blank=True, null=True)
    HR_Review = models.TextField(blank=True, null=True)
    NoOfPasses = models.PositiveIntegerField(blank=True, null=True)
    NoOfFails = models.PositiveIntegerField(blank=True, null=True)
    NoOfOnHolds = models.PositiveIntegerField(blank=True, null=True)
    InterviewNo = models.IntegerField(blank=True, null=True, default=0) #NoOfIntDone + 1 in vacancy NEWLY ADDED FIELD
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return u'{}'.format(self.Vacancy)


class Interview_Interviewer(models.Model):
    Interview = models.ForeignKey(Interview)
    Interviewer = models.ForeignKey(User)

    def __str__(self):
        return self.Interviewer


class Venue(models.Model):
    HallName = models.CharField(max_length=40)

    def __str__(self):
        return self.HallName


class Vacancy(models.Model): #No Of Interviews should come to this vacancy
    DateOfPublish = models.DateField()
    ClosingDate = models.DateField()
    NoOfIntDone = models.IntegerField(default=0) #should be auto increment
    NoOfPossitions = models.IntegerField()
    Post_Dept = models.ForeignKey(Post_Dept, on_delete=models.CASCADE)
    done = models.BooleanField(default=False) #NEWLY ADDED FIELD

    def __str__(self):
        return u'{}'.format(self.Post_Dept)


class Experience(models.Model):
    Post = models.ForeignKey(Post, null=True, blank=True)
    AltPost = models.CharField(max_length=100, null=True, blank=True)
    Field = models.CharField(max_length=100)
    Duration = models.FloatField(max_length=2.2)
    YearStart = models.IntegerField()
    YearEnd = models.IntegerField()
    Company = models.CharField(max_length=100)
    Notes = models.TextField()
    Personal = models.ForeignKey(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return u'{}'.format(self.Personal)


class SubQualification(models.Model):

    QName = models.CharField(max_length=100)
    Subject = models.CharField(max_length=150)
    Result = models.CharField(max_length=10,null=True,blank=True)
    SubResult = models.CharField(max_length=4)
    QType = models.IntegerField() #if educational 1 or if professional 0
    personal = models.ForeignKey("Personal")
    SpecialNotes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Subject


class subQul_Post(models.Model):
    QName = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    SubResult = models.CharField(max_length=10)
    Post = models.ForeignKey(Post)


class Exp_Post(models.Model):
    ExPost = models.ForeignKey(Post, related_name='ExPost')
    Post = models.ForeignKey(Post)
    Duration = models.FloatField(max_length=2.2)

    def __str__(self):
        return self.ExPost


class Messages(models.Model):
    MsgType = models.IntegerField()
    MsgCont = models.TextField(null=True,blank=True)
    MsgAcceptance = models.IntegerField()
    Recieve = models.ForeignKey(User,related_name="Msg_Reciever")
    Send= models.ForeignKey(User)
    SentDate = models.DateField()
    SentTime = models.TimeField()
    RecievedDate = models.DateField(null=True)
    RecievedTime = models.TimeField(null=True)



