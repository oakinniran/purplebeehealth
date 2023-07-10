from .models import Nurse
from rest_framework import serializers


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nurse
        fields='__all__'



        