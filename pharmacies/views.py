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
from .models import Pharmacy
from .serializers import PharmacySerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class PharmacyListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            pharmacies = Pharmacy.objects.all()
            serializer =PharmacySerializer(pharmacies, many=True)
            return Response({"pharmacies":serializer.data})
        except Pharmacy.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = PharmacySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Pharmacy.DoesNotExist:
            return Response(serializer.errors, status=400)



class PharmacyDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        pharmacy = Pharmacy.objects.get(pk=pk)
        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)

    def put(self, request, pk):
        pharmacy = Pharmacy.objects.get(pk=pk)
        serializer = PharmacySerializer(pharmacy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        pharmacy = Pharmacy.objects.get(pk=pk)
        pharmacy.delete()
        return Response(status=204)

