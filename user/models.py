from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    def set_password(self,password):
        self.password=make_password(password)
        self.save()    
        
        
