from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Score

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScoreSerializer

@api_view(['GET'])
def getScores(request):
    scores = Score.objects.all().order_by('-score_value')



    ser = ScoreSerializer(scores, many = True)
    return Response(ser.data)
  
def home(request): 
    return render(request, "cardgame.html") 

@login_required
def games(request): 
    return render(request, "jatekok.html")

@login_required
def leaderboard(request):
    scores = Score.objects.all().order_by('-score_value')
    return render(request, "eredmenytabla.html", {"scores":scores})

@login_required
def snake(request): 
    return render(request, "snake.html")

@login_required
def tictactoe(request): 
    return render(request, "tictactoe.html")



# API ENDPOINT
@login_required
def setScore(request, score):
    s = Score(user = request.user,score_value = score)
    s.save()
    return redirect("leaderboard")
    