import os
import env
import json
import requests

from django.shortcuts import render, reverse, redirect
from .models import Movie
from .forms import AddMovieForm

# A view of the homepage which takes all objects from the database and sends them to the index.html page.
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

def add_movie(request):
    if request.method == "POST":
        add_movie_form = AddMovieForm(request.POST)
        if add_movie_form.is_valid():

            # Setting all the variables before fetching the data from the API
            api_key = os.getenv('API_KEY')
            movie_id = add_movie_form.cleaned_data['search_field']
            url = "http://www.omdbapi.com/?i={0}&apikey={1}".format(movie_id, api_key)

            # Fetching data from API
            data = requests.get(url)

            # Taking usefull data from API and storing it into local database
            new_movie = Movie()
            new_movie.title = data.json()['Title']
            new_movie.plot = data.json()['Plot']
            new_movie.year = data.json()['Year']
            new_movie.rated = data.json()['Rated']
            new_movie.released = data.json()['Released']
            new_movie.director = data.json()['Director']
            new_movie.poster = data.json()['Poster']
            new_movie.imdbid = data.json()['imdbID']
            new_movie.imdbrating = data.json()['Metascore']
            new_movie.save()

            return redirect(reverse('index'))

    else:
        form = AddMovieForm()
        return render(request, "add_movie.html", {'form': form})