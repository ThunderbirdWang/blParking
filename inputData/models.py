from django.db import models
from login.models import ownerUser

# Create your models here.
class ownerInfo(models.Model):
    roomNo=models.CharField(max_length=20,unique=True)
    phoneNo=models.CharField(max_length=20,unique=True)

class carInfo(models.Model):
    carId=models.ForeignKey(ownerUser,on_delete=models.CASCADE)
    numberPlate=models.CharField(max_length=10,unique=True)
