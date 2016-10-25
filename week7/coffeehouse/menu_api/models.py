from django.db import models

# Create your models here.

class Special(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
