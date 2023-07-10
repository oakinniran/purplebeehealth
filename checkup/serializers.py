from .models import CheckupDetail
from rest_framework import serializers


class CheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model=CheckupDetail
        fields='__all__'