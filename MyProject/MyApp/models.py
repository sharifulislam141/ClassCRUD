from django.db import models
from django.urls import reverse

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=60)
    def get_absolute_url(self):
        return reverse('my_app:index')
    def __str__(self):
        return self.first_name+ " "+ self.last_name
    
class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date= models.DateField()
    rating = (
        (1,"Wrost"),
        (2,"Bad"),
        (3,"Not Bad"),
        (4,"Good"),
        (5,"Excellent")
    )
    num_star = models.IntegerField(choices=rating)
    def __str__(self):
        return self.name +" "+ str(self.num_star)
