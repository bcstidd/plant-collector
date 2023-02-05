from django.shortcuts import render

# Create your views here.
plants = [
    {'name': 'Nerve plant', 'plantclass': 'Indoor/tropical', 'thrivesin':'Bright/indirect light', 'difficulty':'Easy'},
    {'name': 'Pothos', 'plantclass': 'Climber', 'thrivesin': 'Bright/indirect light', 'difficulty': 'Easy'},
    {'name': 'Snake Plant', 'plantclass': 'Succulent', 'thrivesin': 'Full sun || Low light', 'difficulty': 'Easy'},
    {'name': 'Giant Chain Fern', 'plantclass': 'Shrub', 'thrivesin': 'Indirect light', 'difficulty': 'Moderate-Hard'},
    {'name': 'Monstera deliciosa', 'plantclass': 'Tropical Shrub/Vine', 'thrivesin': 'Bright/indirect light', 'difficulty': 'Moderate'},
    {'name': 'String of Hearts', 'plantclass': 'Tropical Vine', 'thrivesin': 'Bright/indirect light', 'difficulty': 'Moderate'},

    ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {
        'plants': plants,
    })