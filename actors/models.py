from django.db import models

NATIONALITY_CHOICES = [
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('MX', 'Mexico'),
    ('GB', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('IT', 'Italy'),
    ('JP', 'Japan'),
    ('KR', 'South Korea'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
    ('AU', 'Australia'),
    ('ES', 'Spain'),
    ('RU', 'Russia'),
    ('ZA', 'South Africa'),
    ('NG', 'Nigeria'),
    ('AR', 'Argentina'),
    ('NL', 'Netherlands'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('BE', 'Belgium'),
    ('IE', 'Ireland'),
    ('PT', 'Portugal'),]

class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100,choices=NATIONALITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name
    
