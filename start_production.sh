#!/bin/bash
echo "🚀 Starting Enslin's Beauty Parlor Production System"
echo "==================================================="

# Start backend
echo "🐍 Starting Django Backend..."
cd backend
source venv/bin/activate

python manage.py runserver 8000 &
BACKEND_PID=$!

cd ..

echo ""
echo "🎉 PRODUCTION SYSTEM STARTED!"
echo "============================="
echo "🌐 Website: http://localhost:8000"
echo "🔧 Admin Panel: http://localhost:8000/admin"
echo "📊 API: http://localhost:8000/api"
echo ""
echo "🔑 Admin Credentials:"
echo "   Username: admin"
echo "   Password: KamoAdmin"
echo ""
echo "✨ FEATURES:"
echo "   ✅ React Frontend with iOS 26.1 Animations"
echo "   ✅ Django REST API Backend"
echo "   ✅ Service Booking System"
echo "   ✅ Academy Course Enrollment"
echo "   ✅ Combo Booking Options"
echo "   ✅ Professional Image Gallery"
echo "   ✅ Mobile Responsive Design"
echo ""
echo "Press Ctrl+C to stop the server"

# Handle cleanup
trap "kill $BACKEND_PID; exit" INT
wait
