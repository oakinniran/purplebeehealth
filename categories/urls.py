from django.urls import path
from .views import CategoryList, CategoryDetails


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),

]