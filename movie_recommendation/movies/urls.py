from django.urls import path
from . import views
from .views import movie_detail
from .views import register_view, login_view, logout_view, home

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
