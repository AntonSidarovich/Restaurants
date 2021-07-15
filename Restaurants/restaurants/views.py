from django.shortcuts import render
from .models import Restaurant 
from django.shortcuts import HttpResponse


def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants, 'title': 'Restaurants'})

