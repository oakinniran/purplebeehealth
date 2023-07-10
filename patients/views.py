from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Patients
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes      
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientSerializer

# @csrf_exempt
authentication_classes = ([SessionAuthentication,TokenAuthentication])
permission_classes = [IsAuthenticated] 
def patient_list(request): 
    try:
        patients = Patients.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse({"patients":serializer.data}, safe=False)
    except Patients.DoesNotExist:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
# @csrf_exempt
def patient_detail(request, pk):
    try:
        patient = get_object_or_404(Patients, pk=pk)
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)
    except Patients.DoesNotExist:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
def patient_create(request):
    serializer = PatientSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
def patient_update(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    serializer = PatientSerializer(patient, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

def patient_delete(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    patient.delete()
    return JsonResponse({"message": "Patient deleted successfully"})








# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication       
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import IsAuthenticated
# from datetime import datetime
# import math
# # from django.http import JsonResponse
# from rest_framework import status, generics
# from .models import Patients
# from .serializers import PatientSerializer
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAdminOrReadOnly


# # @csrf_exempt
# class PatientListCreateView(generics.GenericAPIView):
#     authentication_classes = ([SessionAuthentication,TokenAuthentication])
#     permission_classes = [IsAuthenticated] 

#     # serializer_class = PatientSerializer
#     # queryset = Patients.objects.all()

#     # def get(self, request):
#     #     page_num = int(request.GET.get("page", 1))
#     #     limit_num = int(request.GET.get("limit", 10))
#     #     start_num = (page_num - 1) * limit_num
#     #     end_num = limit_num * page_num
#     #     search_param = request.GET.get("search")
#     #     patients = Patients.objects.all()
#     #     total_notes = patients.count()
#     #     if search_param:
#     #         patients = patients.filter(title__icontains=search_param)
#     #     serializer = self.serializer_class(patients[start_num:end_num], many=True)
#     #     return Response({
#     #         "status": "success",
#     #         "total": total_notes,
#     #         "page": page_num,
#     #         "last_page": math.ceil(total_notes / limit_num),
#     #         "patients": serializer.data
#     #     })

#     # def post(self, request):
#     #     serializer = self.serializer_class(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
#     #     else:
#     #         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
#     def get(self, request):
#         try:
#             patients = Patients.objects.all()
#             serializer = PatientSerializer(patients, many=True)
#             return Response({"patients":serializer.data})
#         except Patients.DoesNotExist:
#            return Response(serializer.errors, status=400)   
# # @csrf_exempt
#     def post(self, request):
#         try:
#             serializer = PatientSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             return Response(serializer.errors, status=400)
#         except Patients.DoesNotExist:
#             return Response(serializer.errors, status=400)



# class PatientDetailView(generics.GenericAPIView):
#     authentication_classes = ([SessionAuthentication, TokenAuthentication])
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk):
#         patient = Patients.objects.get(pk=pk)
#         serializer = PatientSerialize(patient)
#         return Response(serializer.data)

#     def put(self, request, pk, *args, **kwargs):
#         patient = Patients.objects.get(pk=pk)
#         serializer = PatientSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)




#     permission_classes = [IsAdminOrReadOnly]
#     def delete(self, request, pk):
        
#         patient = Patients.objects.get(pk=pk)
#         patient.delete()
#         return Response(status=204)



#     # queryset =  Patients.objects.all()
#     # serializer_class = PatientSerializer

#     # def get_note(self, pk):
#     #     try:
#     #         return  Patients.objects.get(pk=pk)
#     #     except:
#     #         return None

#     # def get(self, request, pk):
#     #     patient = self.get_note(pk=pk)
#     #     if patient == None:
#     #         return Response({"status": "fail", "message": f"Patient with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#     #     serializer = self.serializer_class(patient)
#     #     return Response({"status": "success", "data": {"patient": serializer.data}})

#     # def patch(self, request, pk):
#     #     patient = self.get_note(pk)
#     #     if patient == None:
#     #         return Response({"status": "fail", "message": f"Patient with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#     #     serializer = self.serializer_class(
#     #         patient, data=request.data, partial=True)
#     #     if serializer.is_valid():
#     #         serializer.validated_data['updatedAt'] = datetime.now()
#     #         serializer.save()
#     #         return Response({"status": "success", "data": {"patient": serializer.data}})
#     #     return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request, pk):
#     #     patient = self.get_note(pk)
#     #     if patient == None:
#     #         return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#     #     patient.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)




