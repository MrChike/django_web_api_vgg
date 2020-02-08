from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from web_api_app import serializers


class AppViewSet(viewsets.ViewSet):
    serializer_class = serializers.AppSerializer

    def list(self, request):
        list_viewset = [
            'uses actions',
            'maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'list_viewset': list_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # Get object/request by id
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        # Update object/request
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        # part object/request update
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        # Delete object/data
        return Response({'http_method': 'DELETE'})
