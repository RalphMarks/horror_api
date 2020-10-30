from rest_framework.test import APISimpleTestCase
from django.urls import reverse
from django.test import Client

class TestGetHello(APISimpleTestCase):
    """
    test get hello endpoint
    """
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_search_movie(self):
        r = reverse('hello-view')
        response = self.client.get(r)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Hello world o/')