from django.urls import path
from movies.views import MovieListCreateView, MovieDetailView, MovieStatsView


urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie_list_create_view'),  
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail_view'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie_stats_view'),
]