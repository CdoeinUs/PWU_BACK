from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from Account.models import UserRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # 추가 작업
        return response
