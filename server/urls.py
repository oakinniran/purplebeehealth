
from django.contrib import admin
from django.urls import path, re_path, include

from myapp import views
from rest_framework.routers import DefaultRouter
# from s.views import PatientListCreateView, PatientDetailView





urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    re_path('api/specialisations/', include('specialisations.urls')),
    re_path('api/vitalsigns/', include('vitalsign.urls')),
    re_path('api/patients/', include('patients.urls')),
    re_path('api/nurses/', include('nurses.urls')),
    re_path('api/doctors/', include('physicians.urls')),
    re_path('api/pharmacies/', include('pharmacies.urls')),
    re_path('api/prescriptions/', include('prescription.urls')),
    re_path('api/checkups/', include('checkup.urls')),
    re_path('api/inventories/', include('inventories.urls')),
    re_path('api/categories/', include('categories.urls')),



    
    
]




