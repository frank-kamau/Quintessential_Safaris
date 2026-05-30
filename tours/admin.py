from django.contrib import admin

# Register your models here.
from .models import Hotel, Tour

admin.site.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'tour', 'budget_type']
    list_filter = ['budget_type', 'tour']
