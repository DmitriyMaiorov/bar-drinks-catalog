from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # /
    path('drinks/', views.drink_list, name='drink_list'),
    path('drink/<int:id>/', views.drink_detail, name='drink_detail'),
    path('like/<int:id>/', views.like_drink, name='like_drink'),
    path('random/', views.random_drink, name='random_drink'),
    path('search/', views.search, name='search'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:category_id>/', views.drinks_by_category, name='drinks_by_category'),
]
