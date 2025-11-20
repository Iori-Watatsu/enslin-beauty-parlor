from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'duration_weeks', 'price', 'is_active']
    list_filter = ['level', 'is_active']
    search_fields = ['name', 'description']
