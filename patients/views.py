from django.shortcuts import render



# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Patients
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes      
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientSerializer

# @csrf_exempt



class PatientList(generics.ListCreateAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    serializer_class = PatientSerializer
    queryset = Patients.objects.all()

class patientDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    serializer_class = PatientSerializer
    queryset = Patients.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAdminUser] 
        instance = self.get_object()
        if request.user.role != 'admin':  # Check if the author is not the current user
              return Response({"error": "You are not allowed to destroy this instance"})
        request.user.itemdeletedcount+=1
        return super().destroy(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        deleted_by = self.request.user
        instance.createdBy = deleted_by
        instance.itemdeletedcount +=1
        instance.save()
        super().perform_destroy(instance) 
   
