from django.db import models
# from django.contrib.auth.models import Use
from myapp.models import CustomUser
import uuid

# Create your models here.
class Patients(models.Model):
    patientId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    profileImage = models.ImageField(upload_to='item_images', blank=True, null=True)
    scan = models.ImageField(upload_to='scan_images', blank=True, null=True)
    phone=models.CharField(max_length=200)
    gender=models.CharField(max_length=50, null=True)
    createdBy=models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    dateOfBirth = models.DateField()
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add = True, null = True)

    class Meta:
        verbose_name_plural = 'Patients'