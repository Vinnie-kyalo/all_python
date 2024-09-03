from django.shortcuts import render
from .models import (
    FoodInflation,
   
)

def inflation_overview(request):
    context = {
        'food_inflation': FoodInflation.objects.all(),
    }
    return render(request, 'overview.html', context)
