from rest_framework import serializers
from reviews.models import Review
from movies.models import Movie

class ReviewSerializer(serializers.ModelSerializer):
    
    rate = serializers.IntegerField(
        min_value=0,
        max_value=5,
        error_messages={
            'min_value': 'Rate must be between 0 and 5',
            'max_value': 'Rate must be between 0 and 5',
            'required': 'Rate is required',
        })


    class Meta:
        model = Review
        fields = '__all__'

        