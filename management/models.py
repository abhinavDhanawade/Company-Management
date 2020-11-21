from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.

class Employe(models.Model):
    empId= models.CharField(max_length=20, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    dob = models.DateField(null=True)
    city = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.empId


class Managerr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    dob = models.DateField(null=True)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.firstname