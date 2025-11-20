from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import routers
from apps.services.views import ServiceViewSet
from apps.academy.views import CourseViewSet
from apps.bookings.views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'bookings', BookingViewSet)

def api_root(request):
    return JsonResponse({
        "message": "Enslin's Beauty Parlor API",
        "endpoints": {
            "services": "/api/services/",
            "courses": "/api/courses/",
            "bookings": "/api/bookings/",
            "admin": "/admin/"
        }
    })

def frontend(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', frontend),
    path('services/', frontend),
    path('academy/', frontend),
    path('booking/', frontend),
]
