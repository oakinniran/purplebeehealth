from rest_framework import serializers
from .models import Physician

class  PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physician
        fields = '__all__'