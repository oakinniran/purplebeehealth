from django.db import models
from myapp.models import CustomUser
import uuid

# Create your models here.

class Pharmacy(models.Model):
    class Meta:
        verbose_name_plural = 'pharmacies'
    pharmacyID=models.AutoField(primary_key=True)
    name =models.CharField(max_length=250)
    contact=models.TextField(blank=True)
    phone=models.CharField(max_length=100)
    createdBy=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=50, null=True)
    updatedAt = models.DateTimeField(auto_now_add = True, null = True)