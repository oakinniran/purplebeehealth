from django.urls import path
from .views import PrescriptionList, PrescriptionDetails

urlpatterns = [
    path('prescriptions/', PrescriptionList.as_view()),
    path('prescriptions/<int:pk>/', PrescriptionDetails.as_view()),

]