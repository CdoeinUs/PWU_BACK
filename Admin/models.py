from django.db import models

# Create your models here.
class Liquor(models.Model):
    CASE_CHOICES =[
        ('Y', '있음'),
        ('N', '없음'),
    ]
    COUNTRY_CHOICES=[
        ('NOT','불명'),
        ('SCT','스코틀랜드'),
        ('GBR','영국'),
    ]
    TYPE_CHOICES=[
        ('whisky','위스키'),
    ]
    name = models.CharField(max_length=20)
    proof = models.IntegerField(max_length=100)
    image = models.ImageField()
    detail = models.CharField(max_length=20)
    type = models.CharField(choices=TYPE_CHOICES,max_length=20)
    country = models.CharField(choices=CASE_CHOICES, max_length=20)
    amount = models.IntegerField()
    case = models.CharField(max_length=1,choices=CASE_CHOICES)
    price = models.IntegerField()
    reviews = models.IntegerField()
    #likes = 

class Cocktail(models.Model):
    name = models.CharField(max_length=20)
    create = models.DateField()
    proof = models.IntegerField(max_length=100)
    detail = models.TextField()
    image = models.ImageField()
    #elements = models.ForeignKey()
    #likes = 
    