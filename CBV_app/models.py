from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=250)
    grade = models.IntegerField(blank = True)
    location = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    st_name = models.CharField(max_length=250)
    grade = models.IntegerField(blank = True)
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.st_name    
    