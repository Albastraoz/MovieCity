from django.db import models

# This is a model which is used to store data from the API to the database.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField(max_length=1000)
    year = models.CharField(max_length=200)
    rated = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    genre = models.CharField(max_length=200)
    released = models.CharField(max_length=50)
    director = models.CharField(max_length=200)
    actors = models.CharField(max_length=500)
    poster = models.CharField(max_length=500)
    imdbid = models.CharField(max_length=12)
    imdbrating = models.CharField(max_length=4)

    def __str__(self):
        return self.title