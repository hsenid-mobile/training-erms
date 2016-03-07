from django.db import models

# class CreatUser(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     email = models.EmailField()
#     date_joined = models.DateTimeField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.username


class PersonInfo(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    Male = 'Male'
    Female = 'Female'
    gender_choice = (
        (Male, 'Male'),
        (Female, 'Female'))
    gender = models.CharField(max_length=50, choices=gender_choice, default=Male)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    telephone = models.IntegerField()
    # image = models.ImageField()

    def genderClass(self):
        return self.gender in (self.Male, self.Female)

    def __str__(self):
        return self.firstName

class Education(models.Model):
    university = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    average_gpa = models.FloatField()
    from_year = models.DateField()
    to_year = models.DateField()
    description = models.TextField(max_length=200)
    secondary_education = models.CharField(max_length=50)
    gca_al_stream = models.CharField(max_length=20)
    gca_ol_stream = models.TextField(max_length=10)

    def __str__(self):
        return self.university

class Projects(models.Model):
    undergraduate_projects = models.TextField(max_length=500)
    other_projects = models.TextField(max_length=500)


class SampleMode(models.Model):
    name = models.CharField(max_length= 20)
    age = models.IntegerField()
    email = models.EmailField()
    telephone = models.IntegerField()

    def __str__(self):
        return self.name

