from django.shortcuts import render
from django.contrib.auth.decorators import login_required
  
def home(request): 
    return render(request, "cardgame.html") 

@login_required
def games(request): 
    return render(request, "jatekok.html")

@login_required
def leaderboard(request): 
    return render(request, "eredmenytabla.html")

@login_required
def snake(request): 
    return render(request, "snake.html")

@login_required
def tictactoe(request): 
    return render(request, "tictactoe.html")