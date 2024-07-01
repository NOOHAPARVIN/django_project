from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]