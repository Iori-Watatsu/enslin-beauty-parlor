from django.db import models
from apps.services.models import Service
from apps.academy.models import Course

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    SERVICE_TYPE_CHOICES = [
        ('SERVICE', 'Beauty Service'),
        ('COURSE', 'Academy Course'),
        ('COMBO', 'Service Combo'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    combo_services = models.ManyToManyField(Service, related_name='combo_bookings', blank=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.PositiveIntegerField(help_text="Total duration in minutes")
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.get_service_type_display()} - {self.booking_date}"

    class Meta:
        ordering = ['-booking_date', '-booking_time']
