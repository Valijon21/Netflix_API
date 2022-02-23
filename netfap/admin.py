
from django.contrib import admin
from .models import Actor,Movie
# Register your models here.

@admin.register(Movie)

class MoveiAdmin(admin.ModelAdmin):
    list_display=['name','year','imdb']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    
    list_display = ['name','birth_date',] 
   