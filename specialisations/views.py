from .models import Specialisation
from .serializers import SpecialisationSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions




class SpecializationList(generics.ListCreateAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    permission_classes = [IsAuthenticated]
    serializer_class = SpecialisationSerializer
    queryset = Specialisation.objects.all()

class SpecializationDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ([SessionAuthentication,TokenAuthentication])
    serializer_class = SpecialisationSerializer
    permission_classes = [IsAuthenticated] 
    queryset = Specialisation.objects.all()
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.role != 'admin':  # Check if the author is not the current user
              return Response({"error": "You are not allowed to destroy this instance"})
        request.user.itemdeletedcount+=1
        return super().destroy(request, *args, **kwargs)

    
    # def perform_destroy(self, instance):
    #     if request.user.role == 'admin': 
    #     # deleted_by = self.request.user
    #     # instance.deleted_by = deleted_by
    #         request.user.itemdeletedcount +=1
    #         instance.save()
    #         super().perform_destroy(instance)
   

