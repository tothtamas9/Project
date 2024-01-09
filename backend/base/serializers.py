from rest_framework.serializers import ModelSerializer
from .models import Score

class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'
        depth = 1