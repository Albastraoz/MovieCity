import os
import env
import json
import requests

from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Movie
from .forms import SearchForm

# A view of the homepage which takes all objects from the database and sends them to the index.html page.
def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

def search_movie(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():

            # Setting all the variables before fetching the data from the API
            api_key = os.getenv('API_KEY')
            search_key = search_form.cleaned_data['search_field']

            # Creating URL and request data from the API
            search_url = "http://www.omdbapi.com/?s={0}&apikey={1}".format(search_key, api_key)
            search_results = requests.get(search_url)

            # Put search results into json data
            search_data = search_results.json()['Search']

            form = SearchForm()
            return render(request, "search.html", {'results': search_data, 'form': form})
    else:
        form = SearchForm()
        return render(request, "search.html", {'form': form})

def add_movie(request, id):
    if request.method == "POST":
        # Setting API key and creating URL
        api_key = os.getenv('API_KEY')
        url = "http://www.omdbapi.com/?i={0}&plot=full&apikey={1}".format(id, api_key)

        # Fetching data from API
        data = requests.get(url)

        # Taking usefull data from API and storing it into local database
        new_movie = Movie()
        new_movie.title = data.json()['Title']
        new_movie.plot = data.json()['Plot']
        new_movie.year = data.json()['Year']
        new_movie.country = data.json()['Country']
        new_movie.genre = data.json()['Genre']
        new_movie.rated = data.json()['Rated']
        new_movie.released = data.json()['Released']
        new_movie.director = data.json()['Director']
        new_movie.actors = data.json()['Actors']
        new_movie.poster = data.json()['Poster']
        new_movie.imdbid = data.json()['imdbID']
        new_movie.imdbrating = data.json()['Metascore']
        new_movie.save()
        return redirect(reverse('index'))

    else:
        return redirect(reverse('search_movie'))

def delete_movie(request, id):
    # Remove a movie from the list
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect(index)