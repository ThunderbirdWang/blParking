from django.db import models

# Create your models here.
class blParkingDb(models.Model):
    roomNo=models.CharField(max_length=20)
    phoneNo=models.IntegerField()