from django.urls import path
from .views import VitalSignList, VitalSignDetails

urlpatterns = [
    path('vitalsigns/', VitalSignList.as_view()),
    path('vitalsigns/<int:pk>/', VitalSignDetails.as_view()),

]