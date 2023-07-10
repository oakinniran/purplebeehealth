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
from .models import Physician
from .serializers import PhysicianSerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class PhysiciantListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            doctors = Physician.objects.all()
            serializer =PhysicianSerializer(doctors, many=True)
            return Response({"doctors":serializer.data})
        except Physician.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = PhysicianSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Physician.DoesNotExist:
            return Response(serializer.errors, status=400)



class PhysicianDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        doctor = Physician.objects.get(pk=pk)
        serializer = PhysicianSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = Physician.objects.get(pk=pk)
        serializer = PhysicianSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        doctor = Physician.objects.get(pk=pk)
        doctor.delete()
        return Response(status=204)
