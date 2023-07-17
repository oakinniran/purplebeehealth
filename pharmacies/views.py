from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import Pharmacy
from .serializers import PharmacySerializer
from rest_framework.permissions import IsAuthenticated


class PharmacyList(generics.ListCreateAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Pharmacy.objects.all()
        sex=self.request.query_params.get('gender')
        if sex is not None:
            queryset= queryset.filter(gender=sex)
        return queryset

    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()

class PharmacyDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()
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


