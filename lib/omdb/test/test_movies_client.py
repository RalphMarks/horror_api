from rest_framework.test import APISimpleTestCase
from django.urls import reverse
from django.test import Client
from lib.omdb.movies import MoviesClient
from unittest.mock import patch

class TestMoviesCLient(APISimpleTestCase):
    """
    test movie client
    """

    @patch('requests.get')
    def test_movie_client_successfull_request(self, mocked_get):
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {'Response': 'True'}
        movie_client = MoviesClient('b9b0224b')
        response, status = movie_client.search(None)
        self.assertEqual(status, 200)

    @patch('requests.get')
    def test_movie_client_bad_request(self, mocked_get):
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {'Response': 'False', 'Error': 'error'}
        movie_client = MoviesClient('b9b0224b')
        response, status = movie_client.search(None)
        self.assertEqual(response, 'error')
        self.assertEqual(status, 400)
