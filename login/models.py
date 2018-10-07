from django.db import models

# Create your models here.
class ownerUser(models.Model):
    phoneNo=models.CharField(max_length=20,unique=True)
    pwd=models.CharField(max_length=256)

