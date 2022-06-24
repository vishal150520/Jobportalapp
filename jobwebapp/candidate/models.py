from django.db import models
class applyjob(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dateofbirth=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    percentage=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contactno=models.CharField(max_length=50)
    jonid=models.CharField(max_length=50)
    projectdetails=models.CharField(max_length=50)