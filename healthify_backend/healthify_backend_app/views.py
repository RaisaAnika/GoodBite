#from django.shortcuts import render
# healthify_backend_app/views.py
# views.py

from django.http import HttpResponse
from rest_framework import generics
from .models import FoodItem, HealthifiedOption
from .serializers import FoodItemSerializer, HealthifiedOptionSerializer
from django.http import JsonResponse
from .openai_integration import openai_request
from django.http import JsonResponse
from .openai_integration import call_palm_api
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
    


def healthify_view(request):
    if request.method == 'POST':
        food_item = request.POST.get('food_item')  # Get the user's input
        diet_type = request.POST.get('diet_type')  # Get the diet type from the frontend

        # Call the PaLM API function with food_item and diet_type
        result = call_palm_api(food_item, diet_type)

        # Return the result to the frontend
        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)

