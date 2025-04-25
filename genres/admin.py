from django.contrib import admin
from genres.models import Genres

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')