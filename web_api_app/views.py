from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from web_api_app import serializers
from web_api_app import models
from web_api_app import permissions


class UsersProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersProfileSerializer
    queryset = models.Users.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UsersUpdateProfile,)


class UsersAuthApiView(ObtainAuthToken):
    # Create authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProjectsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProjectsSerializer
    queryset = models.Projects.objects.all()

    def perform_create(self, serializer):
        # assign correct user profile when logged in
        serializer.save(user_profile=self.request.user)
