from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'service_type', 'booking_date', 'booking_time', 'status']
    list_filter = ['service_type', 'status', 'booking_date']
    search_fields = ['customer_name', 'customer_email']
