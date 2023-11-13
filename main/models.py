from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.TextField(max_length=50)
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    is_new = models.BooleanField(default=True)
    rarity = models.CharField(max_length=10)

