from __future__ import unicode_literals

from django.db import models


class PersonInfo(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Address = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

#Login
class LogMode(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=50)
    def __str__(self):
        return self.Username