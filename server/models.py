from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
# 



class CustomUser(AbstractUser):
    # Add/modify fields here
    custom_role = models.CharField(max_length=255)