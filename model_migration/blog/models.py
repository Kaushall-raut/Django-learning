from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(20)
    age=models.IntegerField()
    city=models.CharField(20)  
    # used to convert the query set into readable format

def __str__(self):
    return self.name