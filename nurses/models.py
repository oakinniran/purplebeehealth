from django.db import models
from myapp.models import CustomUser

# Create your models here.

class Nurse(models.Model):
    class Meta:
        verbose_name_plural = 'nurses'


    nurseID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact=models.TextField(blank=True, null=True)
    phone=models.CharField(max_length=100)
    created_by=models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    gender=models.CharField(max_length=50, null=True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    

