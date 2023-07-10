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
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class PrescriptionListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            prescriptions = Prescription.objects.all()
            serializer =PrescriptionSerializer(prescriptions, many=True)
            return Response({"prescriptions":serializer.data})
        except Prescription.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = PrescriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Prescription.DoesNotExist:
            return Response(serializer.errors, status=400)



class PrescriptionDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        presciption = Prescription.objects.get(pk=pk)
        serializer = PrescriptionSerializer(presciption)
        return Response(serializer.data)

    def put(self, request, pk):
        presciption = Prescription.objects.get(pk=pk)
        serializer = PrescriptionSerializer(presciption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        presciption = Prescription.objects.get(pk=pk)
        presciption.delete()
        return Response(status=204)


