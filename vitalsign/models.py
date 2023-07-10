from django.db import models
from patients.models import Patients
from specialisations.models import Specialisation
from myapp.models import CustomUser

# Create your models here.

class VITALSIGN(models.Model):
    specialisatiion= models.ForeignKey(Specialisation, on_delete=models.CASCADE)
    vitalSignId=models.AutoField(primary_key=True)
    bloodPressure = models.IntegerField()
    weight=models.CharField(max_length=200)
    pulseRate=models.FloatField()
    height=models.CharField(max_length=200)
    temperature=models.CharField(max_length=200)
    created_by=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patientId= models.ForeignKey(Patients, related_name='patients', on_delete=models.CASCADE)
    bloodSugar=models.CharField(max_length=200)

# Create your models here.
