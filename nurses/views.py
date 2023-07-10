from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Nurse
from .serializers import NurseSerializer
from rest_framework.permissions import IsAuthenticated



class NurseSignCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            nurses =  Nurse.objects.all()
            serializer = NurseSerializer(nurses, many=True)
            return Response({"nurses":serializer.data})
        except  Nurse.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = NurseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except  Nurse.DoesNotExist:
            return Response(serializer.errors, status=400)



class NurseSignDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        nurse =  Nurse.objects.get(pk=pk)
        serializer = VitalSignSerialize(nurse)
        return Response(serializer.data)

    def put(self, request, pk):
        patient =  Nurse.objects.get(pk=pk)
        serializer = NurseSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        patient =  Nurse.objects.get(pk=pk)
        patient.delete()
        return Response(status=204)
