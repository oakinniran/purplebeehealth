from django.urls import path
from .views import PatientList, patientDetails

urlpatterns = [
    path('patients/', PatientList.as_view()),
    path('patients/<int:pk>/', patientDetails.as_view()),

]