from django.urls import include, path
from rest_framework import routers
from allauth.account.views import confirm_email
from .views import RegistrationViewSet, ConfirmEmailViewSet

router = routers.DefaultRouter()

router.register(r'register', RegistrationViewSet, basename='register')
