from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:pk>/', views.tour_detail, name='tour_detail'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
]
