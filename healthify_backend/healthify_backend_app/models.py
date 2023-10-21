# from django.db import models

# Create your models here.
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.PositiveIntegerField()
    # Add other fields as needed

class HealthifiedOption(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    alternative_name = models.CharField(max_length=100)
    alternative_description = models.TextField()
    alternative_calories = models.PositiveIntegerField()
    # Add other fields as needed
