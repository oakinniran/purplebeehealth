from django.urls import path
from .views import InventoryList, InventoryDetails

urlpatterns = [
    path('inventories/', InventoryList.as_view()),
    path('inventories/<int:pk>/', InventoryDetails.as_view()),

]