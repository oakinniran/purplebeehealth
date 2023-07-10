from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'custom_role']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password', None)  # Remove 'password' field from the representation
        return representation
