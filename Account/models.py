from django.db import models
from django.contrib.auth.models import AbstractUser
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from Admin.models import Liquor,Cocktail


class User(AbstractUser):
    # Add custom fields here
    nickname = models.CharField(max_length=30, blank=True)
    liked_liquor = models.ManyToManyField(Liquor, null=True,related_name='like_liquor')
    liked_cocktail = models.ManyToManyField(Cocktail,null=True,related_name='like_liquor')

    class Meta:
        # Change related_name for groups and user_permissions
        permissions = (("can_view_user", "Can view user"),)
        default_permissions = ()
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class UserRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=30)

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
        }

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save(update_fields=['nickname'])

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'nickname')