from rest_framework import serializers
from .models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['patientId', 'name', 'email', 'address', 'profileImage', 'scan', 'phone', 'created_by', 'dateOfBirth', 'createdAt','updated_at']