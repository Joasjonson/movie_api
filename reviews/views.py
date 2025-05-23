from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission



class ReviewListCreateView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer