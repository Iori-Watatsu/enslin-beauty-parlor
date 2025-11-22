from django.db import migrations

def create_services(apps, schema_editor):
    Service = apps.get_model('services', 'Service')

    services = [
        {
            'name': 'Professional Hair Styling',
            'category': 'HAIR',
            'description': 'Expert haircuts, coloring, and styling for any occasion',
            'duration': 60,
            'price': 450.00,
            'image_url': 'https://images.unsplash.com/photo-1560066984-138dadb4c035?w=400',
            'is_active': True
        },
        {
            'name': 'Luxury Nail Art & Care',
            'category': 'NAILS',
            'description': 'Creative nail designs with premium products and care',
            'duration': 45,
            'price': 350.00,
            'image_url': 'https://images.unsplash.com/photo-1583305728936-39199cd8b69f?w=400',
            'is_active': True
        },
        {
            'name': 'Professional Makeup Artistry',
            'category': 'MAKEUP',
            'description': 'Flawless makeup application for events and special occasions',
            'duration': 90,
            'price': 600.00,
            'image_url': 'https://images.unsplash.com/photo-1512496015859-f55c42f17c6f?w=400',
            'is_active': True
        },
        {
            'name': 'Skin Rejuvenation Facial',
            'category': 'SKIN',
            'description': 'Advanced facial treatments for radiant, healthy skin',
            'duration': 75,
            'price': 550.00,
            'image_url': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=400',
            'is_active': True
        },
        {
            'name': 'Full Body Relaxation Massage',
            'category': 'SPA',
            'description': 'Therapeutic massage for complete relaxation and stress relief',
            'duration': 60,
            'price': 400.00,
            'image_url': 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=400',
            'is_active': True
        },
        {
            'name': 'Complete Bridal Package',
            'category': 'BRIDAL',
            'description': 'Full bridal package including hair, makeup, and trial sessions',
            'duration': 180,
            'price': 1500.00,
            'image_url': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?w=400',
            'is_active': True
        }
    ]

    for service_data in services:
        Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
    print("✅ Services created successfully!")

def create_courses(apps, schema_editor):
    Course = apps.get_model('academy', 'Course')

    courses = [
        {
            'name': 'Advanced Makeup Artistry',
            'description': 'Master advanced makeup techniques for professional work',
            'duration_weeks': 8,
            'price': 7500.00,
            'level': 'ADVANCED',
            'image_url': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400',
            'curriculum': 'Color Theory|Advanced Techniques|Special Effects|Business Skills',
            'requirements': 'Basic makeup knowledge required',
            'is_active': True
        },
        {
            'name': 'Nail Technician Certificate',
            'description': 'Become a certified nail technician through hands-on training',
            'duration_weeks': 6,
            'price': 3500.00,
            'level': 'BEGINNER',
            'image_url': 'https://images.unsplash.com/photo-1607778835362-66d246bea575?w=400',
            'curriculum': 'Nail Anatomy|Manicure Techniques|Nail Art|Sanitation',
            'requirements': 'No experience required',
            'is_active': True
        },
        {
            'name': 'Skincare Specialist Course',
            'description': 'Comprehensive training in facial treatments and skincare',
            'duration_weeks': 10,
            'price': 6000.00,
            'level': 'INTERMEDIATE',
            'image_url': 'https://images.unsplash.com/photo-1596704012031-3d84a30c0c60?w=400',
            'curriculum': 'Skin Analysis|Facial Techniques|Product Knowledge|Client Care',
            'requirements': 'Basic beauty knowledge',
            'is_active': True
        }
    ]

    for course_data in courses:
        Course.objects.get_or_create(
            name=course_data['name'],
            defaults=course_data
        )
    print("✅ Courses created successfully!")

class Migration(migrations.Migration):
    dependencies = [
        ('services', '0001_initial'),
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_services),
        migrations.RunPython(create_courses),
    ]
