
# from django.contrib import admin
# from django.urls import path, re_path, include

# from myapp import views
# from rest_framework.routers import DefaultRouter
# from s.views import PatientListCreateView, PatientDetailView





# urlpatterns = [
#     path('admin/', admin.site.urls),
#     re_path('signup', views.signup),
#     re_path('login', views.login),
#     re_path('test_token', views.test_token),
#     re_path('api/specialisations/', include('specialisations.urls')),
#     re_path('api/vitalsigns/', include('vitalsign.urls')),
#     re_path('api/patients/', include('patients.urls')),
#     re_path('api/nurses/', include('nurses.urls')),
#     re_path('api/doctors/', include('physicians.urls')),
#     re_path('api/pharmacies/', include('pharmacies.urls')),
#     re_path('api/prescriptions/', include('prescription.urls')),
#     re_path('api/checkups/', include('checkup.urls')),
#     re_path('api/inventories/', include('inventories.urls')),
#     re_path('api/categories/', include('categories.urls')),

    
# ]
from django.contrib import admin
from myapp import views
from django.urls import path, re_path, include
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Other URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
    # Other URLs
]