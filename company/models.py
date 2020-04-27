from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=100)
    websiteurl=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

class Company_skills(models.Model):
    skill=models.CharField(max_length=100)
    company_uname=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)

class Company_notice(models.Model):
    internships=models.CharField(max_length=1000,default=None)
    placements=models.CharField(max_length=1000,default=None)
    company_unam=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
