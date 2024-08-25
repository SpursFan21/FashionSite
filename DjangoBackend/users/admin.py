
# admin.py

from django.contrib import admin
from .models import CustomUser, UserProfile, Role, UserRole, PasswordReset

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(PasswordReset)
