from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser as User

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                if user.is_active:
                    return user
                else:
                    # User is inactive
                    return user
            else:
                # Password is incorrect
                return None
        except User.DoesNotExist:
            # User does not exist
            return None
