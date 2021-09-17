from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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
