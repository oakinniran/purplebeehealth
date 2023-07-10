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
from .models import VITALSIGN
from .serializers import VitalSignSerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class VitalSignCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            vitalsigns = VITALSIGN.objects.all()
            serializer = VitalSignSerializer(vitalsigns, many=True)
            return Response({"vitalsigns":serializer.data})
        except VITALSIGN.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = VitalSignSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except VITALSIGN.DoesNotExist:
            return Response(serializer.errors, status=400)


# @csrf_exempt
class VitalSignDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        vitalsign = VITALSIGN.objects.get(pk=pk)
        serializer = VitalSignSerialize(vitalsign)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = VITALSIGN.objects.get(pk=pk)
        serializer = VitalSignSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        patient = VITALSIGN.objects.get(pk=pk)
        patient.delete()
        return Response(status=204)
