from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    message=models.TextField()

class Add_Details(models.Model):
    student_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    yop=models.CharField(max_length=50)

class Course(models.Model):
    first_name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=10)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    add = models.TextField()
    course = models.CharField(max_length=30)

