from django.contrib import admin
from ManageUsers.models import UserProfile, UserType, UserRole

admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(UserType)


