
from django.contrib import admin
from django.urls import path, re_path, include

from myapp import views
from rest_framework.routers import DefaultRouter
from specialisations.views import SpecialisationListCreateView, SpecialisationDetailView
from vitalsign.views import VitalSignCreateView, VitalSignDetailView
# from patients.views import PatientListCreateView, PatientDetailView
from nurses.views import NurseSignCreateView, NurseSignDetailView
from physicians.views import PhysiciantListCreateView, PhysicianDetailView
from pharmacies.views import PharmacyListCreateView, PharmacyDetailView
from prescription.views import PrescriptionListCreateView, PrescriptionDetailView
from checkup.views import CheckupListCreateView, CheckupDetailView
from categories.views import CategoryListCreateView, CategoryDetailView
from inventories.views  import InventoryListCreateView, inventoryDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    re_path('api/specialisations/', SpecialisationListCreateView.as_view(), name='specialisation-list-create'),
    re_path('api/specialisations/<int:pk>/', SpecialisationDetailView.as_view(), name='specialisation-detail'),
    re_path('api/vitalsigns/', VitalSignCreateView.as_view(), name='citalsign-list-create'),
    re_path('api/vitalsigns/<int:pk>/', VitalSignDetailView.as_view(), name='vital-detail'),
    # re_path('api/patients/', PatientListCreateView.as_view(), name='patient_list'),
    # re_path('api/patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('api/patients/', include('patients.urls')),
    re_path('api/nurses/', NurseSignCreateView.as_view(), name='nurse_list'),
    re_path('api/nurses/<int:pk>/', NurseSignDetailView.as_view(), name='nurse_detail'),
    re_path('api/doctors/', PhysiciantListCreateView.as_view(), name='doctor_list'),
    re_path('api/doctors/<int:pk>/', PhysicianDetailView.as_view(), name='doctor_detail'),
    re_path('api/pharmacies/', PharmacyListCreateView.as_view(), name='pharmacy_list'),
    re_path('api/pharmacies/<int:pk>/', PharmacyDetailView.as_view(), name='pharmacy_detail'),
    re_path('api/prescriptions/', PrescriptionListCreateView.as_view(), name='prescription_list'),
    re_path('api/prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
    re_path('api/checkups/', CheckupListCreateView.as_view(), name='checkup_list'),
    re_path('api/checkups/<int:pk>/', CheckupDetailView.as_view(), name='checkup_detail'),
    re_path('api/categories/', CategoryListCreateView.as_view(), name='categories_list'),
    re_path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='categories_detail'),
    re_path('api/categories/', InventoryListCreateView.as_view(), name='inventories_list'),
    re_path('api/categories/<int:pk>/', inventoryDetailView.as_view(), name='inventories_detail'),


    
    
]




