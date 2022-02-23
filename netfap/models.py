from django.db import models

# Create your models here.
GENDER_CHOICES = [
    ('M','MEN'),
     ('W','WOMEN'),
]
GENRE = [
    ('M','Melodramma'),
    ('R','Romantic'),
    ('C','Comedy'),
    ('D','Dramma'),
    ('F','Fantasy')
    
]
class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.DateField(auto_now_add=True)
    imdb = models.IntegerField()
    genre = models.CharField(choices=GENRE,max_length=1)
    cust = models.ManyToManyField('Actors')
    
    def __str__(self):
        return self.name
    
class Actors(models.Model):
    
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    films = models.ManyToManyField(Movie)
    def __str__(self):
        return self.name
        