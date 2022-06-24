from django.db import models

# Create your models here.
class candidate(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dateofbirth=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    percentage=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contactno=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    projectdetails=models.CharField(max_length=50)

class company(models.Model):
    companyname=models.CharField(max_length=50)
    companygstno=models.CharField(max_length=50)
    hrmfname=models.CharField(max_length=50)
    hrmlname=models.CharField(max_length=50)
    dateofbirth=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    empid=models.CharField(max_length=50)
    contactno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    jobdescription=models.CharField(max_length=50)