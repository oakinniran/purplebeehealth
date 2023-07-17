from django.urls import path
from .views import PharmacyList, PharmacyDetails

urlpatterns = [
    path('pharmacies/', PharmacyList.as_view()),
    path('pharmacies/<int:pk>/', PharmacyDetails.as_view()),

]