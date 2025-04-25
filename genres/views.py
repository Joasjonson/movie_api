from rest_framework import generics
from .models import Genres
from .serializer import GenresSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission


class GenreListCreateView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    



class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]   
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    

    


