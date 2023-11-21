from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("", views.home, name="home"), 
    path("games/", views.games, name="games"), 
    path("leaderboard/", views.leaderboard, name="leaderboard"), 
    path("snake/", views.snake, name="snake"), 
    path("tictactoe/", views.tictactoe, name="tictactoe"), 
]