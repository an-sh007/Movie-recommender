from django.urls import path
from . import views
from .views import movie_detail, register_view, login_view, logout_view, home

urlpatterns = [
    path('', login_view, name='login'),  # Set login as the default page
    path('home/', home, name='home'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
