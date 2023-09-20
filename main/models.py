from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.TextField()
    version = models.TextField()
    releasedate = models.TextField()