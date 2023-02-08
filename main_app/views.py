from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView
from .models import Plant, Admirer
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
    id_list = plant.admirers.all().values_list('id')
    unassigned_admirers = Admirer.objects.exclude(id__in=id_list)
    thirsty_form = ThirstyForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'thirsty_form': thirsty_form,
    'plant': plant, 'thirsty_form': thirsty_form, 'admirers': unassigned_admirers
    })

def add_thirsty(request, plant_id):
    form = ThirstyForm(request.POST)
    if form.is_valid():
        new_thirsty = form.save(commit=False)
        new_thirsty.plant_id = plant_id
        new_thirsty.save()
    return redirect('detail', plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'category', 'thrivesIn', 'difficulty' ]
    success_url = '/plants'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['category', 'difficulty']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'


class AdmirerList(ListView):
  model = Admirer

class AdmirerDetail(DetailView):
  model = Admirer

class AdmirerCreate(CreateView):
  model = Admirer
  fields = '__all__'

class AdmirerUpdate(UpdateView):
  model = Admirer
  fields = ['name', 'location']

class AdmirerDelete(DeleteView):
  model = Admirer
  success_url = '/admirers'

def assoc_admirer(request, plant_id, admirer_id):
    Plant.objects.get(id=plant_id).admirers.add(admirer_id)
    return redirect('detail', plant_id=plant_id)

def disassoc_admirer(request, plant_id, admirer_id):
    Plant.objects.get(id=plant_id).admirers.remove(admirer_id)
    return redirect('detail', plant_id=plant_id)

