from django.db import models

# Create your models here.
class joblist(models.Model):
    jobid=models.CharField(max_length=50)
    jobdesc=models.CharField(max_length=300)