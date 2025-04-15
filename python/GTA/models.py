from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=50)
    message = models.TextField(default=1000)


class Std_form(models.Model):
    
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField(default=18)
    gender = models.CharField(max_length=100)
    enrollmentNumber = models.TextField(unique=True)
    contact = models.IntegerField(default=15)
    course = models.CharField(max_length=200)

    
class crud(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    photo = models.ImageField(upload_to="crud")


# class login(models.Model):
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.TextField(unique=True)


