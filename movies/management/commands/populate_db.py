from django.core.management.base import BaseCommand
from faker import Faker
import random

from genres.models import Genres
from actors.models import Actor
from movies.models import Movie
from reviews.models import Review

fake = Faker()

NATIONALITIES = [code for code, _ in Actor._meta.get_field('nationality').choices]

# List of movie titles
movie_titles = [
    'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 
    'Forrest Gump', 'Inception', 'Fight Club', 'The Matrix', 'Interstellar', 'Gladiator'
]

class Command(BaseCommand):
    help = 'Populates the database with realistic fake data for genres, actors, movies, and reviews'

    def handle(self, *args, **kwargs):
        # Create basic genres
        genre_names = [
            'Action', 'Drama', 'Comedy', 'Romance', 'Sci-Fi', 
            'Horror', 'Adventure', 'Animation', 'Thriller', 'Fantasy'
        ]
        genres = [Genres.objects.get_or_create(name=name)[0] for name in genre_names]

        # Create actors
        actors = []
        for _ in range(20):
            actor = Actor.objects.create(
                name=fake.name(),
                birthday=fake.date_of_birth(minimum_age=20, maximum_age=80),
                nationality=random.choice(NATIONALITIES)
            )
            actors.append(actor)

        # Create movies
        movies = []
        for _ in range(10):
            genre = random.choice(genres)
            title = random.choice(movie_titles)  
            movie = Movie.objects.create(
                title=title,
                genre=genre,
                release_date=fake.date_between(start_date='-50y', end_date='today'),
                resume=fake.text(max_nb_chars=250)
            )
            movie.actors.set(random.sample(actors, k=random.randint(1, 4)))
            movies.append(movie)

        # Create reviews
        for movie in movies:
            for _ in range(random.randint(1, 5)):
                Review.objects.create(
                    movie=movie,
                    rate=random.randint(0, 5),
                    comment=fake.sentence()
                )

        self.stdout.write(self.style.SUCCESS('Database successfully populated with fake movie data!'))
