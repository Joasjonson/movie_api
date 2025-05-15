from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializer import GenresSerializer
from actors.models import Actor
from actors.serializer import ActorSerializer

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("Release date must be after 1950.")
        return value

    def validate_title(self, value):
        if Movie.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError("Movie with this title already exists.")
        return value
    

class MovieListSerializer(serializers.ModelSerializer):
    genre = GenresSerializer()
    actors = ActorSerializer(many=True)
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'resume', 'release_date', 'avg_rate']
   
    def get_avg_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('rate'))['rate__avg']
        if rate:
            return round(rate, 1)
        return 0.0
