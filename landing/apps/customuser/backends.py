from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model


class EmailBackend(object):

    def authenticate(self, **kwargs):
        User = get_user_model()
        email = kwargs.get('email')
        password = kwargs.get('password')
        try:
            if email:
                user = User.objects.get(
                    email=BaseUserManager.normalize_email(email)
                )
                if user.check_password(password):
                    return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
