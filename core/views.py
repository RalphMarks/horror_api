from rest_framework.views import APIView
from rest_framework.response import Response
from lib.omdb.movies import MoviesClient
class MoviesView(APIView):
    """
    Movie view
    """

    def get(self, request):
        """
        Get movies
        """
        search = request.query_params.get('search', None)
        movies_client = MoviesClient('b9b0224b')
        data, status = movies_client.search(search)
        return Response(data=data, status=status)