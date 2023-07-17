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
from rest_framework import generics, permissions



class InventoryList(generics.ListCreateAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Inventory.objects.all()
        category=self.request.query_params.get('category')
        if category is not None:
            queryset= queryset.filter(category=category)
        return queryset

    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

class InventoryDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

    def destroy(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAdminUser] 
        instance = self.get_object()
        if request.user.role != 'admin':  # Check if the author is not the current user
              return Response({"error": "You are not allowed to destroy this instance"})
        request.user.itemdeletedcount+=1
        return super().destroy(request, *args, **kwargs)
    
    # def perform_destroy(self, instance):
    #     deleted_by = self.request.user
    #     instance.createdBy = deleted_by
    #     instance.itemdeletedcount +=1
    #     instance.save()
    #     super().perform_destroy(instance) 
