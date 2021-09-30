from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField

# Create your models here.
class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name