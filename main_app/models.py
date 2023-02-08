from django.db import models
from django.urls import reverse

DRINKS = (
    ('F', 'Fine'),
    ('W', 'Watered'),
    ('N', 'Not Watered'),
)

# Create your models here.
class Admirer(models.Model):
    name = models.TextField(max_length=50)
    location = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admirers_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thrivesIn = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)
    admirers = models.ManyToManyField(Admirer)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

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
