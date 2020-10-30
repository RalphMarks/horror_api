"""
omdb movies client
"""
import requests
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .client import OMDBClient
from .exceptions import OMDBBadRequestException

class MoviesClient(OMDBClient):
    """
    search for movies using omdb api
    """

    def __init__(self, api_key):
        super(MoviesClient, self).__init__(api_key)

    def search(self, search):

        try:
            self.get(f'{self.url}t={search}')
        except Exception as exc:
            return exc.detail, status.HTTP_400_BAD_REQUEST
        return self.service_response.json(), status.HTTP_200_OK
