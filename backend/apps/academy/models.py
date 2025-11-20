from django.db import models

class Course(models.Model):
    LEVEL_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
        ('PROFESSIONAL', 'Professional'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image_url = models.URLField(blank=True, null=True)
    curriculum = models.TextField(help_text="Course outline and modules")
    requirements = models.TextField(help_text="Prerequisites")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.level}"

    class Meta:
        ordering = ['level', 'name']
