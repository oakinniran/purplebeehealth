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
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class InventoryListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            inventories = Inventory.objects.all()
            serializer = InventorySerializer(inventories, many=True)
            return Response({"inventories":serializer.data})
        except Inventory.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = InventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Inventory.DoesNotExist:
            return Response(serializer.errors, status=400)



class inventoryDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        inventory = Inventory.objects.get(pk=pk)
        serializer = PatientSerialize(inventory)
        return Response(serializer.data)

    def put(self, request, pk):
        inventory = Inventory.objects.get(pk=pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        inventory = Inventory.objects.get(pk=pk)
        inventory.delete()
        return Response(status=204)
