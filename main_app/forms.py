# forms.py

from django.forms import ModelForm
from .models import Thirsty

class ThirstyForm(ModelForm):
  class Meta:
    model = Thirsty
    fields = ['date', 'water']
