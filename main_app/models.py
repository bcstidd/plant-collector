from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thrivesIn = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)

    def __str__(self):
        return self.name