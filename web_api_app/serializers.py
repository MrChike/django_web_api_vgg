from rest_framework import serializers


class AppSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
