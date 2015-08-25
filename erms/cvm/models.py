from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date published')
    nationality = models.CharField(max_length=200)
    nic_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
