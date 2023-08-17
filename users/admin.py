from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # List of fields to display in the User list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'address', 'phonenumber', 'dob', 'is_staff', 'is_active')
    # Fields to search in the User list view
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Fieldsets to organize fields in the User detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'address', 'phonenumber', 'dob')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Customize the User add view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    # Ordering of User list view
    ordering = ('-date_joined',)

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
