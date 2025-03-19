from django.urls import path
from . import views
from .views import movie_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
]
