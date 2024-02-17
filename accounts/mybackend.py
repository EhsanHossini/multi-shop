# from django.contrib.auth.backends import ModelBackend
# from .models import MyUser


# class MobileBackend(ModelBackend):
#     def user_can_authenticate(self, username=None, password=None, **kwargs):
#         mobile = kwargs['mobile']
#         try:
#             user = MyUser.objects.get(mobile=mobile)
#         except MyUser.DoesNotExist:
#             pass


from django.contrib.auth.backends import ModelBackend
from .models import User


class MobileBackend(ModelBackend):
    def user_can_authenticate(self, username=None, password=None, **kwargs):
        mobile = kwargs['number']
        try:
            user = User.objects.get(number=number)
        except User.DoesNotExist:
            pass