from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score_value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score_value}"