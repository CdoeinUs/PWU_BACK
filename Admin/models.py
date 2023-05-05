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
    proof = models.IntegerField()
    image = models.ImageField(("image") , blank=True, height_field=None, width_field=None, max_length=None)  
    type = models.CharField(choices=TYPE_CHOICES,max_length=20)
    country = models.CharField(choices=CASE_CHOICES, max_length=20)
    amount = models.IntegerField()
    case = models.CharField(max_length=1,choices=CASE_CHOICES)
    price = models.IntegerField()
    reviews = models.IntegerField()
    #likes = 

class Cocktail(models.Model):    
    TYPE_CHOICES=[
        ('Whisky','위스키'),
        ('Bodka','보드카'),
        ('Gin','진'),        
        ('Rum','럼'),
        ('Tequila','데킬라'),
    ]
    name = models.CharField(max_length=20)
    image = models.ImageField(max_length=None)
    detail = models.TextField(max_length=200)
    base = models.CharField(choices=TYPE_CHOICES, max_length=20,default=0)
    #elements = models.ForeignKey()
    #likes = 
    