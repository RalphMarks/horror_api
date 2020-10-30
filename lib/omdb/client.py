"""
OMDB client requests
"""
import requests
from django.conf import settings
from .exceptions import (OMDBBadRequestException, OMDBServiceUnavailable)

class OMDBClient:
    """
    Client class for making requests to omdb
    """

    def __init__(self, api_key):

        self.service_response = None
        self.service_response_status_code = None
        self.base_url = settings.OMDB_BASE_URL
        self.url=f'{self.base_url}?apikey={api_key}&'

    def get(self, url, **kwargs):
        """
        Get request to omdb
        """
        self.service_response = requests.get(url, **kwargs)
        return self._handle_response()

    def _handle_response(self):
        """
        Handle response errors
        """

        if self.service_response is not None:
            json = self.service_response.json()

            if(json['Response'] == 'True'):
                return self
            else:
                raise OMDBBadRequestException(detail=json['Error'])
        else:
            raise OMDBServiceUnavailable()
