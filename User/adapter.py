from Admin.models import Liquor,Cocktail
from allauth.account.adapter import DefaultAccountAdapter
from django.db import models

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        liked_liquor = models.ManyToManyField(Liquor,blank=True)
        liked_cocktail = models.ManyToManyField(Cocktail,blank=True)
        if commit:
            user.save()
        return user
