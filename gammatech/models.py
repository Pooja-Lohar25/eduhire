from django.db import models

# Create your models here.
class users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    phone = models.IntegerField(max_length=10)
    faculty = models.BooleanField(default=True)
