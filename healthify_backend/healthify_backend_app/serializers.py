# serializers.py
from rest_framework import serializers
from .models import FoodItem, HealthifiedOption

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class HealthifiedOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthifiedOption
        fields = '__all__'