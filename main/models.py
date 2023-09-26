from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.TextField()
    version = models.TextField()
    releasedate = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
