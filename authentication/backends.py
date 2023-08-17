from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

CustomUser = get_user_model()

class CustomUserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the input is a valid email format
            if '@' in username:
                user = CustomUser.objects.get(email=username)
            else:
                user = CustomUser.objects.get(username=username)
            
            # Exclude superusers and staff members from authentication
            if user.is_active and not user.is_superuser and not user.is_staff:
                if user.check_password(password):
                    return user
        except CustomUser.DoesNotExist:
            return None
        
              # Additional check for superusers and staff members
        if user.is_superuser or user.is_staff:
            if user.check_password(password):
                return user

        return None


    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        
    