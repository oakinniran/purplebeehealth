from django.db import models
from physicians.models import Physician

# Create your models here.

class CheckupDetail(models.Model):
    class Meta:
        verbose_name_plural = 'diagnoses'
    
    diagnosesID =models.AutoField(primary_key=True)
    diagnoses = models.TextField()
    doctor=models.ForeignKey(Physician,  on_delete=models.CASCADE, null=True)
    doctorRemark=models.TextField()
    location=models.CharField(max_length=200)
    prescription=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)

