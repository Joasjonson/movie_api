from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rate', 'created_at')
    search_fields = ('movie__title',)
    list_filter = ('rate', 'created_at')
    ordering = ('-created_at',)
