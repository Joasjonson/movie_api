from genres.models import Genres
from rest_framework import serializers

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'name']