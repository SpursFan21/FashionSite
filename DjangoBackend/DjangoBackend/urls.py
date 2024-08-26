from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include URLs from the users app
]
