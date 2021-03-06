from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API view """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over application logic',
            'Is manually mapped to URLs',
            ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview })

    def post(self, request):
        """create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handles partial updates for objects"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Handles deleting objects"""
        return Response({'method' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message' : message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ handles getting an object by id"""
        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """handles updating an object"""
        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """handles a partial update of an object"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """handles deleting an object"""
        return Response({'http_method' : 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating a User Profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
