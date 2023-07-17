from django.urls import path
from .views import PhysicianList, PhysicianDetails

urlpatterns = [
    path('doctors/', PhysicianList.as_view()),
    path('doctors/<int:pk>/', PhysicianDetails.as_view()),

]