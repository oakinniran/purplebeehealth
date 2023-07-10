from django.db import models

class Specialisation(models.Model):
    specialisationID=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
