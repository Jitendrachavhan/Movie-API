from django.urls import path
from api.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('api/movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-retrieve-update-destroy'),
]
