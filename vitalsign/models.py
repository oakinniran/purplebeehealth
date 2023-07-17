from django.db import models

from specialisations.models import Specialisation
from patients.models import Patients
from myapp.models import CustomUser
import uuid

# Create your models here.

class VITALSIGN(models.Model):
    vitalSignId=models.AutoField(primary_key=True)
    specialisatiion= models.ForeignKey(Specialisation, on_delete=models.CASCADE)
    bloodPressure = models.IntegerField()
    weight=models.CharField(max_length=200)
    pulseRate=models.FloatField()
    height=models.CharField(max_length=200)
    temperature=models.CharField(max_length=200)
    createdAt=models.DateTimeField(auto_now_add=True)
    createdBy=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient= models.ForeignKey(Patients, related_name='patients', on_delete=models.CASCADE)
    bloodSugar=models.CharField(max_length=200)
    updatedAt = models.DateTimeField(auto_now_add = True, null = True)

# Create your models here.
