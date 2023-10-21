# healthify_backend_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('food_items/', views.FoodItemList.as_view(), name='food-item-list'),
    path('healthified_options/', views.HealthifiedOptionList.as_view(), name='healthified-option-list'),
    path('', views.home, name='home'),
    path('openai/', views.openai_view, name='openai-view')

]


