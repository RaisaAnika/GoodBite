#from django.shortcuts import render


# views.py

from django.http import HttpResponse
from rest_framework import generics
from .models import FoodItem, HealthifiedOption
from .serializers import FoodItemSerializer, HealthifiedOptionSerializer
from django.http import JsonResponse
from .openai_integration import openai_request

class FoodItemList(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class HealthifiedOptionList(generics.ListCreateAPIView):
    queryset = HealthifiedOption.objects.all()
    serializer_class = HealthifiedOptionSerializer
    


def home(request):
    return HttpResponse("Welcome to Healthify App")

def openai_view(request):
    if request.method == 'POST':
        # Send a request to OpenAI using the function from openai_integration.py
        response = openai_request()
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)