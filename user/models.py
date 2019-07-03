from django.db import models

from django.contrib.auth.models import AbstractBaseUser
class profile(AbstractBaseUser):
    username = models.CharField('username', max_length=10, unique=True,db_index=True, default = 'noob')
    
    email = models.EmailField(unique=True)
    
    password = models.CharField( max_length = 20)
    mobilenumber = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'

class login(models.Model):
    username = models.CharField(max_length=200)
    Password=models.CharField(max_length=20)





    

