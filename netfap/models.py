from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M','MEN'),
     ('W','WOMEN'),
]
GENRE = [
    ('',''),
    
]
class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.DateField(auto_now_add=True)
    imdb = models.models.IntegerField()
    genre = models.models.CharField(max_length=1)
    
       
    
class Actor(models.Model):
    
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
        