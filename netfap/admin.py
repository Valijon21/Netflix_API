
from django.contrib import admin
from .models import Actors,Movie
# Register your models here.

@admin.register(Movie)

class MoveiAdmin(admin.ModelAdmin):
    list_display=['name','year','imdb']

@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    
    list_display = ['name','birth_date',] 
   