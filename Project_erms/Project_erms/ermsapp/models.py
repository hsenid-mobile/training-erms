from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Person_{0}/{1}'.format(instance.Person.id, filename)


class Person(models.Model):
    NIC = models.PositiveIntegerField(unique=True)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    FullName = models.CharField(max_length=100)
    DOB = models.DateField()
    Nationality = models.CharField(max_length=20)
    CVImage = models.FileField(upload_to=user_directory_path)
    Department = models.ManyToManyField("Department")
    Post = models.ManyToManyField("Post")
    Experience = models.ManyToManyField("Experience",through="Person_Experience")
    Qualifications = models.ManyToManyField("Qualifications",through="Person_Qualifications")

    def __unicode__(self):
        return self.FName,self.LName,self.FullName,self.Nationality



class Department(models.Model):
    DeptName = models.CharField(max_length=30)

    def __unicode__(self):
        return self.DeptName


class InterviewType(models.Model):
    InterviewType = models.CharField(max_length=30)

    def __unicode__(self):
        return self.InterviewType


class Post(models.Model):
    Post = models.CharField(max_length=100)
    NoOfInterviews = models.PositiveIntegerField()
    InterviewType = models.ManyToManyField(InterviewType,through="Post_IntType")
    Experience = models.ManyToManyField("Experience",through="Post_Experience")

    def __unicode__(self):
        return self.Post


class Post_IntType(models.Model):
    PostID = models.ForeignKey(Post,on_delete=models.CASCADE)
    InterviewTypeID = models.ForeignKey(InterviewType,on_delete=models.CASCADE)


class Degree(models.Model):
    University = models.CharField(max_length=30)
    Degree = models.CharField(max_length=30)
    DegreeType = models.CharField(max_length=10)
    Post_Degree = models.ManyToManyField(Post, through='Post_Degree')

    def __unicode__(self):
        return self.University,self.Degree,self.DegreeType


class Post_Degree(models.Model):
    PostID = models.ForeignKey(Post,on_delete=models.CASCADE)
    DegreeID = models.ForeignKey(Degree, on_delete=models.CASCADE)
    Year = models.DateField()
    SpecialNotes = models.TextField()
    GPA = models.FloatField()


class Users(models.Model):
    UName = models.CharField(max_length=30)
    Password = models.CharField(max_length=3)
    FName =  models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    Post =  models.ForeignKey(Post)
    Department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.UName,self.FName,self.Password,self.LName

    class Meta:
        abstract = True


class Interviewers(Users):
    InterviewerID = models.PositiveIntegerField(primary_key=True)
    NoOfInts = models.PositiveIntegerField()
    SpecializedArea = models.ManyToManyField('SpecializedArea',through="Interviewers_SpecializedArea")


class HOD(Users):
    HODID = models.PositiveIntegerField(primary_key=True)


class HR(Users):
    HRID = models.PositiveIntegerField(primary_key=True)


class Admin(Users):
    AdminID = models.PositiveIntegerField(primary_key=True)


class SpecializedArea(models.Model):
    SpecializedAreaID = models.PositiveIntegerField(primary_key=True)
    SpecializedArea = models.CharField(max_length=100)


class Interviewers_SpecializedArea(models.Model):
    Interviewers = models.ForeignKey(Interviewers,on_delete=models.CASCADE)
    SpecializedArea = models.ForeignKey(SpecializedArea,on_delete=models.CASCADE)


class Interview(models.Model):
    Time = models.TimeField()
    Date = models.DateField()
    Venue = models.ForeignKey('Venue')
    HOD = models.ForeignKey(HOD)
    Post = models.ForeignKey(Post)
    Vacancy = models.ForeignKey('Vacancy')
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    InterviewType = models.ForeignKey(InterviewType, on_delete=models.CASCADE)


class Venue(models.Model):
    HallName = models.CharField(max_length=40)

    def __unicode__(self):
        return self.HallName


class Vacancy(models.Model):
    DateOfPublish = models.DateField()
    ClosingDate = models.DateField()
    NoOfIntDone = models.IntegerField()
    NextInterview = models.ForeignKey(Post_IntType)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE)


class Experience(models.Model):
    Post = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Post,self.Type


class Person_Experience(models.Model):
    Experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Duration = models.DateField()


class Post_Experience(models.Model):
    Experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    Person = models.ForeignKey(Post,on_delete=models.CASCADE)
    Duration = models.DateField()


class Qualifications(models.Model):
    QName = models.CharField(max_length=100)
    Result = models.CharField(max_length=20)

    def __unicode__(self):
        return self.QName,self.Result


class SubQualification(models.Model):
    Subject = models.CharField(max_length=200)
    SubResult = models.CharField(max_length=4)
    SubWiseResQualifications = models.ForeignKey(Qualifications)

    def __unicode__(self):
        return self.Subject,self.SubResult


class Person_Qualifications(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Qualifications = models.ForeignKey(Qualifications,on_delete=models.CASCADE)
