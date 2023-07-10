from django.db import models
from categories.models import Category
from myapp.models import CustomUser

# Create your models here.

class Inventory(models.Model):
    class Meta:
        verbose_name_plural = 'inventories'

    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=225)
    description=models.TextField(blank=True, null=True)
    unit_price=models.FloatField()
    is_available=models.BooleanField(default=False)
    quantity=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='item_images', blank=True, null=True)