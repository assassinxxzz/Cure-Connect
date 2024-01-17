from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    add=models.TextField()

class Patient(models.Model):
    first_name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    aadharnumber = models.CharField(max_length=12)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    add = models.TextField()
    symptoms = models.TextField()

    # Emergency Details
    ename = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)  
    emergencynumber = models.CharField(max_length=10)

class Feed(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    msg=models.TextField()

class Hospitalinfo(models.Model):
    hospitalname=models.CharField(max_length=50)
    doctorname=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    area=models.TextField()
    location=models.TextField()
    link=models.URLField()

class Appointmentinfo(models.Model):
    hospitalname=models.CharField(max_length=50)
    location=models.TextField()
    link=models.URLField()

# Create your models here.s

