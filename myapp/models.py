from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models



class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural='users'
    # Add/modify fields here
    # groups = models.ManyToManyField(Group, related_name='customuser_set')
    # user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')
    role = models.CharField(max_length=255, default="", blank=True, null=True)
    itemdeletedcount= models.IntegerField(default=0, blank=True, null=True)