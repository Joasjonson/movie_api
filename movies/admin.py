from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'resume')
    search_fields = ('title',)
    list_filter = ('release_date',)
