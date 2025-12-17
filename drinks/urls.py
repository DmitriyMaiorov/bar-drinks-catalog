from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('drink/<int:id>/', views.drink_detail, name='drink_detail'),
    path('like/<int:id>/', views.like_drink, name='like_drink'),
    path('search/', views.search, name='search'),
    path('categories/', views.categories, name='categories'),
]
