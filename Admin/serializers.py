from rest_framework import serializers
from .models import Liquor,Cocktail

class LiquorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Liquor
        fields = ['id', 'name', 'proof', 'image', 'type', 'country', 'amount', 'case', 'price', 'reviews']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        else:
            return None


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'