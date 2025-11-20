from rest_framework import serializers
from .models import Booking
from apps.services.serializers import ServiceSerializer

class BookingSerializer(serializers.ModelSerializer):
    service_details = ServiceSerializer(source='service', read_only=True)
    combo_services_details = ServiceSerializer(source='combo_services', many=True, read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
