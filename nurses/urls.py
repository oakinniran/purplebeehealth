from django.urls import path
from .views import NurseList, NurseDetails

urlpatterns = [
    path('nurses/', NurseList.as_view()),
    path('nurses/<int:pk>/', NurseDetails.as_view()),

]