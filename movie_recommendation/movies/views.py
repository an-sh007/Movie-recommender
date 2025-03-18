from django.shortcuts import render
from .models import Movie
import random

def home(request):
    # Fetch all movies
    movies = Movie.objects.all()

    # Select 3 random movies for recommendations
    recommended_movies = random.sample(list(movies), min(3, len(movies)))

    return render(request, 'movies/home.html', {'movies': movies, 'recommended_movies': recommended_movies})

# Create your views here.
