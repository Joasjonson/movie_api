from rest_framework import generics, views, status
from rest_framework.response import Response
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from app.permission import GlobalDefaultPermission
from django.db.models import Avg
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, GlobalDefaultPermission]
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListSerializer
        return MovieSerializer
    

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_genres = self.queryset.values('genre').distinct().count()

        total_reviwews = Review.objects.all().count()
        avg_rate = round(Review.objects.aggregate(avg_rate=Avg('rate'))['avg_rate'] or 0, 2)

        return Response(
            data={
                'total_movies': total_movies,
                'movies_genres': movies_genres,
                'total_reviwews': total_reviwews,
                'avg_rate': avg_rate},
                
                status=status.HTTP_200_OK)

     

    
