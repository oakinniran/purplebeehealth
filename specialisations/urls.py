from django.urls import path
from .views import SpecializationList, SpecializationDetails

urlpatterns = [
    path('specialisations/', SpecializationList.as_view()),
    path('specialisations/<int:pk>/', SpecializationDetails.as_view()),

]