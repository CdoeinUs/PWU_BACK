from django.shortcuts import render
from rest_framework import generics
from .models import Liquor,Cocktail
from .serializers import LiquorSerializer,CocktailSerializer

class LiquorList(generics.ListCreateAPIView):
    queryset = Liquor.objects.all()
    serializer_class = LiquorSerializer

class LiquorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Liquor.objects.all()
    serializer_class = LiquorSerializer

class CocktailList(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
