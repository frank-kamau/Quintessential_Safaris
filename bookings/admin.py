from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'tour', 'email', 'phone', 'persons', 'booked_on')

    search_fields = ('full_name', 'email', 'reference')