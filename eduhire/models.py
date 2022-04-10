from django.db import models


class Candidate(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length = 10)
    domain = models.CharField(max_length = 150)
    experience = models.IntegerField(default = 0)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    cur_sal = models.IntegerField(default = 0)
    exp_sal = models.IntegerField(default = 0)


class Institute(models.Model):
    insId = models.IntegerField()
    password = models.CharField(max_length = 15)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    category = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)

class Vacancy(models.Model):
    vacId = models.IntegerField()
    experience = models.IntegerField(default = 0)
    contact = models.IntegerField()
    subject = models.CharField(max_length = 100)
    domain = models.CharField(max_length = 100)

class CandHire(models.Model):
    userId = models.IntegerField()
    vacId = models.IntegerField()
    is_hired = models.BooleanField(default = False)
