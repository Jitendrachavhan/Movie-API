from django.contrib import admin

# Register your models here.

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'genre', 'release_date',  'director']

admin.site.register(Movie,MovieAdmin)