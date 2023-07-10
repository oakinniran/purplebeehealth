from django.db import models

# Create your models here.
from django.db import models
from physicians.models import Physician
from checkup.models import CheckupDetail
from pharmacies.models  import Pharmacy
from patients.models import Patients

# Create your models here.

class Prescription(models.Model):
    class Meta:
        verbose_name_plural = 'prescriptions'
    
    prescriptionID =models.AutoField(primary_key=True)
    doctor=models.ForeignKey(Physician,  on_delete=models.CASCADE, null=True)
    diagnosesID=models.ForeignKey(CheckupDetail, related_name='checkup_id', on_delete=models.CASCADE, null= True)
    drugName=models.CharField(max_length=200)
    prescription=models.TextField()
    pharmacyID=models.ForeignKey(Pharmacy, on_delete=models.CASCADE, null= True)
    patientID=models.ForeignKey(Patients, on_delete=models.CASCADE, null= True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
