from django.db import models

# Create your models here.



class login(models.Model): #30
    username = models.CharField(max_length=50)  #30
    password = models.CharField(max_length=50)  #30