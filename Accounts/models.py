from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname = None, password =None,**extra_fields):
        if not email:
            raise ValueError('이메일 항목 누락')
        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, nickname =None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,nickname,password,**extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length= 10,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #liked_liquor = models.ManyToManyField()
    #liked_cocktail = models.ManyToManyField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']


    def __str__(self) :
        return self.id

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)