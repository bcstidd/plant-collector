from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Plant
from .forms import ThirstyForm
# Create your views here.

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
    thirsty_form = ThirstyForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'thirsty_form': thirsty_form})

def add_thirsty(request, plant_id):
    form = ThirstyForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_thirsty = form.save(commit=False)
        new_thirsty.plant_id = plant_id
        new_thirsty.save()
    return redirect('detail', plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['category', 'difficulty']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'
