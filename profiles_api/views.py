from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """ Testing API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of characteristics of the APIView """
        an_apiview = [
            'HTTP Methods used as functions (get, post, patch, put, delete)',
            'Similar to traditional Django views',
            'Full Control over app logic',
            'Manually mapped to URLs'
        ]

        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })

    def post(self, request):
        """ Creates a message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Manages the update of an object """
        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):
        """ Manages a partial update of an object """
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk=None):
        """ Deletes an object """
        return Response({
            'method': 'DELETE'
        })


class HelloViewSet(viewsets.ViewSet):
    """ Test APIView Set """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return message of 'Hello World' """

        a_viewset = [
            'Use actions (list, create, retrieve, update, partial_update)',
            'Automatically map the URLs using routers',
            'Provides more functionality with less code',
        ]

        return Response({
            'message': 'Hola!',
            'a_viewset': a_viewset,
        })

    def create(self, request):
        """ Create new message of 'Hello World' """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Returns an object and his id """

        return Response({
            'http_method': 'GET'
        })

    def update(self, request, pk=None):
        """ Updates an object """

        return Response({
            'http_method': 'PUT'
        })

    def partial_update(self, request, pk=None):
        """ Partially updates an object """

        return Response({
            'http_method': 'PATCH'
        })

    def destroy(self, request, pk=None):
        """ Deletes an object """

        return Response({
            'http_method': 'DELETE'
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Create and update viewSets """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """ Create user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Manages the creation, reading and update of a profile feed """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,
                          IsAuthenticated, )

    def perform_create(self, serializer):
        """ Sets the user profile for the user thats logged in """
        serializer.save(user_profile=self.request.user)
