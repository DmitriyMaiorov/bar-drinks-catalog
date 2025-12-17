from django.urls import path
from .views import drink_list, drink_detail

urlpatterns = [
    path('', drink_list, name='drink_list'),
    path('<int:pk>/', drink_detail, name='drink_detail'),
]