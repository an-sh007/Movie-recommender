from django.shortcuts import render
from .models import Movie

def home(request):
    genre_query = request.GET.get('genre', '')
    rating_query = request.GET.get('rating', '')
    
    movies = Movie.objects.all()
    
    if genre_query:
        movies = movies.filter(genre__icontains=genre_query)
    
    if rating_query:
        try:
            rating = float(rating_query)
            movies = movies.filter(rating__gte=rating)  # Get movies with rating >= input
        except ValueError:
            pass  # Ignore invalid rating inputs

    return render(request, 'movies/home.html', {'movies': movies})
