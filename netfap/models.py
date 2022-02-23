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
    cust = models.ManyToManyField('Actor',blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Filmlar'    
class Actor(models.Model):
    
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    films = models.ManyToManyField(Movie,blank=True)
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name='Aktyorlar'    