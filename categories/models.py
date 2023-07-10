from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'categories'

    def __self__(self):
        return self.name