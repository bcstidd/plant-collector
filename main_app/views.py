from django.shortcuts import render
from .models import Plant
# Create your views here.
plants = [
    {'name': 'Nerve plant', 'category': 'Indoor/tropical', 'thrivesIn':'Bright/indirect light', 'difficulty':'Easy'},
    {'name': 'Pothos', 'category': 'Climber', 'thrivesIn': 'Bright/indirect light', 'difficulty': 'Easy'},
    {'name': 'Snake Plant', 'category': 'Succulent', 'thrivesIn': 'Full sun || Low light', 'difficulty': 'Easy'},
    {'name': 'Giant Chain Fern', 'category': 'Shrub', 'thrivesIn': 'Indirect light', 'difficulty': 'Moderate-Hard'},
    {'name': 'Monstera deliciosa', 'category': 'Tropical Shrub/Vine', 'thrivesIn': 'Bright/indirect light', 'difficulty': 'Moderate'},
    {'name': 'String of Hearts', 'category': 'Tropical Vine', 'thrivesIn': 'Bright/indirect light', 'difficulty': 'Moderate'},

    ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants,
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})
