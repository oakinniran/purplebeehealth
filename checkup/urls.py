from django.urls import path
from .views import CheckupList, CheckupDetails

urlpatterns = [
    path('checkups/', CheckupList.as_view()),
    path('checkups/<int:pk>/', CheckupDetails.as_view()),

]