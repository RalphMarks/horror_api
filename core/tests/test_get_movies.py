from rest_framework.test import APISimpleTestCase
from django.urls import reverse
from django.test import Client

class TestGetMovies(APISimpleTestCase):
    """
    test get movies endpoint
    """
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_search_movie(self):
        r = reverse('movies-view')
        response = self.client.get(r, {'search': 'scooby'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Title', response.data)
        self.assertIn('Year', response.data)
        self.assertIn('Rated', response.data)
        self.assertIn('Runtime', response.data)
        self.assertIn('Genre', response.data)
        self.assertIn('Director', response.data)

    def test_no_search_movie(self):
        r = reverse('movies-view')
        response = self.client.get(r, {'search': 'xxxxxxxxx'})
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, 'Movie not found!')