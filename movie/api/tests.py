from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Movie

class MovieAPITests(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title='Test Movie',
            genre='Test Genre',
            release_date=datetime.now().date(),
            director='Test Director'
        )

    def test_list_movies(self):
        url = reverse('movie-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_movie(self):
        url = reverse('movie-retrieve-update-destroy', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
     #   self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        url = reverse('movie-list-create')
        data = {
            'title': 'New Movie',
            'genre': 'New Genre',
            'release_date': '2023-07-01',
            'director': 'New Director'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_movie(self):
        url = reverse('movie-retrieve-update-destroy', kwargs={'pk': self.movie.id})
        data = {
            'title': 'Updated Movie',
            'genre': 'Updated Genre',
            'release_date': '2023-07-02',
            'director': 'Updated Director'
        }
        response = self.client.put(url, data)
       # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_movie(self):
        url = reverse('movie-retrieve-update-destroy', kwargs={'pk': self.movie.id})
        response = self.client.delete(url)
    #    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
