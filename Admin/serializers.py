from rest_framework import serializers
from .models import Liquor,Cocktail

class LiquorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquor
        fields = '__all__'

class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'