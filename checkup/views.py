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
from .models import CheckupDetail
from .serializers import CheckupSerializer
from rest_framework.permissions import IsAuthenticated


# @csrf_exempt
class CheckupListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
  
    def get(self, request):
        try:
            diagnoses = CheckupDetail.objects.all()
            serializer =CheckupSerializer(diagnoses, many=True)
            return Response({"diagnoses":serializer.data})
        except CheckupDetail.DoesNotExist:
           return Response(serializer.errors, status=400)   
# @csrf_exempt
    def post(self, request):
        try:
            serializer = CheckupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except CheckupDetail.DoesNotExist:
            return Response(serializer.errors, status=400)



class CheckupDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        diagnosis = CheckupDetail.objects.get(pk=pk)
        serializer = CheckupSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, pk):
        diagnosis = CheckupDetail.objects.get(pk=pk)
        serializer = CheckupSerializer(diagnosis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        diagnosis = CheckupDetail.objects.get(pk=pk)
        diagnosis.delete()
        return Response(status=204)


