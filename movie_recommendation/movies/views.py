from django.shortcuts import render, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm

def home(request):
    genre_query = request.GET.get('genre', '')
    rating_query = request.GET.get('rating', '')
    movies = Movie.objects.all()

    if genre_query:
        movies = movies.filter(genre__icontains=genre_query)
    
    if rating_query:
        try:
            rating = float(rating_query)
            movies = movies.filter(rating__gte=rating)
        except ValueError:
            pass

    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    # Handle review form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })
