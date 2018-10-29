from django.contrib.auth.backends import ModelBackend

from .models import MyUser


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(username=username)
            print(user.username)
        except Exception:
            try:
                user = MyUser.objects.get(phone=username)
                print(user.username)
            except Exception:
                return None

        if user.check_password(password):
            return user
        else:
            return None