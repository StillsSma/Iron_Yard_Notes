from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()

class Special(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    ingredients = models.ManyToManyField(Ingredient)

    @property
    def calorie_count(self):
        return 10
