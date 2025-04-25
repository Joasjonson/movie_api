from actors.models import Actor
from actors.serializer import ActorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission


class ActorListCreateView(generics.ListCreateAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission] 
    


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]