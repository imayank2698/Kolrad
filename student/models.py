from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    contact=models.FloatField()
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    pic_path=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.username

class Academicprofile(models.Model):
    ssc=models.CharField(max_length=5)
    hsc=models.CharField(max_length=5)
    cgpa=models.CharField(max_length=5)
    department=models.CharField(max_length=20)
    division=models.CharField(max_length=5)
    rollno=models.CharField(max_length=5)
    desc=models.CharField(max_length=500)
    sum=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return str(self.student_id)


class Internship(models.Model):
    type=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    pic_path=models.CharField(max_length=40)
    desc=models.CharField(max_length=500)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

class Project(models.Model):
    projectname=models.CharField(max_length=20)
    github=models.CharField(max_length=40)
    desc=models.CharField(max_length=500)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

class Skills(models.Model):
    skill=models.CharField(max_length=20)
    rate=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
