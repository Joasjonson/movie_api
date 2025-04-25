from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    rate = models.IntegerField( validators=[MinValueValidator(0, message='Rate must be between 0 and 5'), 
                                            MaxValueValidator(5, message='Rate must be between 0 and 5')] , 
                                            default=0, verbose_name='Rating',
                                            help_text='Rate the movie from 0 to 5')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.rate < 0 or self.rate > 5:
            raise ValidationError('Rate must be between 0 and 5')
        

    def __str__(self):
        return f'{self.movie.title} - {self.rate}'
