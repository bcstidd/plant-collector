from django.db import models
from django.urls import reverse

DRINKS = (
    ('F', 'Fine'),
    ('W', 'Watered'),
    ('N', 'Not Watered'),
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thrivesIn = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Thirsty(models.Model):
    date = models.DateField('Date Watered')
    water = models.CharField(
        max_length=1,
        choices=DRINKS,
        default=DRINKS[0][0]
    )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_water_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
