from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/update/<int:pk>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:pk>/', views.patient_delete, name='patient_delete'),
]
