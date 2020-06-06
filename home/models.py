from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField(max_length=500)
    year = models.IntegerField(max_length=10)
    rated = models.CharField(max_length=10)
    released = models.CharField(max_length=50)
    director = models.CharField(max_length=200)
    poster = models.CharField(max_length=500)
    imdbid = models.CharField(max_length=12)
    imdbrating = models.CharField(max_length=4)

    def __str__(self):
        return self.title
