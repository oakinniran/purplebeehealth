from .models import Category
from .serializers import CategorySerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        specialisations = Category.objects.all()
        serializer = CategorySerializer(specialisations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CategoryDetailView(APIView):
    authentication_classes = ([SessionAuthentication, TokenAuthentication])
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk):
        categories = Category.objects.get(pk=pk)
        categories = CategorySerializer(categories)
        return Response(categories.data)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        category = CategorySerializer(category, data=request.data)
        if category.is_valid():
            category.save()
            return Response(categories.data)
        return Response(category.errors, status=400)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=204)