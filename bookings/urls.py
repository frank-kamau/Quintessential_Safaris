from django.urls import path

from . import views
from .views import booking_success

urlpatterns = [
    path('success/', views.booking_success, name='booking_success'),
    path("search/", views.search_booking, name="search_booking"),
    path('receipt/<str:reference>/',views.booking_receipt_pdf,name='booking_receipt_pdf'),
]
