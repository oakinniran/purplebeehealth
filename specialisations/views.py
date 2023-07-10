from .models import Specialisation
from .serializers import SpecialisationSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SpecialisationListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        specialisations = Specialisation.objects.all()
        serializer = SpecialisationSerializer(specialisations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpecialisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SpecialisationDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk):
        specialisation = Specialisation.objects.get(pk=pk)
        serializer = SpecialisationSerializer(specialisation)
        return Response(serializer.data)

    def put(self, request, pk):
        specialisation = Specialisation.objects.get(pk=pk)
        serializer = SpecialisationSerializer(specialisation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        specialisation = Specialisation.objects.get(pk=pk)
        specialisation.delete()
        return Response(status=204)