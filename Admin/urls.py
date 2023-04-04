from django.urls import include, path
from .views import LiquorList,CocktailList

urlpatterns = [
    path('liquor/',LiquorList.as_view(),),
    path('cocktail/',CocktailList.as_view(),),
]