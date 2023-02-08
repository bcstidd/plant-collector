from django.contrib import admin

from .models import Plant, Thirsty

admin.site.register(Plant)
# register the new Feeding Model 
admin.site.register(Thirsty)