from django.db import models

# Create your models here.
class Student(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=20,default="unknown")

    def __str__(self):
        return self.name