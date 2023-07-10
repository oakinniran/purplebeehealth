from rest_framework import serializers
from .models import VITALSIGN

class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VITALSIGN
        fields = '__all__'