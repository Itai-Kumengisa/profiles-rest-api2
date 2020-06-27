from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view """

    def get(self, request, format=None):
        """return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is manually mapped to URLs',
            ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview })
