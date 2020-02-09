from rest_framework import serializers
from . import models


class UsersProfileSerializer(serializers.ModelSerializer):
    # Link to Users database model

    class Meta:
        model = models.Users
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # create user to db via web_api
    def create(self, validated_data):
        user = models.Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
