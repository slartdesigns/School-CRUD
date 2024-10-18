from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser

class emailBackend(ModelBackend):
    def authenticate(self, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None