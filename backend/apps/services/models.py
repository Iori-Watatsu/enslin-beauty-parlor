from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('HAIR', 'Hair Services'),
        ('NAILS', 'Nail Services'),
        ('MAKEUP', 'Makeup Services'),
        ('SKIN', 'Skin Treatments'),
        ('SPA', 'Spa Services'),
        ('BRIDAL', 'Bridal Packages'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - R{self.price}"

    class Meta:
        ordering = ['category', 'name']
