from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, models


class CreateClientView(APIView):
    """
    API for add client to DB

    Example of POST method:
        {
        "phone": "79831575107",
        "code_of_mobile_operator": 983,
        "tag": "qwerty",
        "timezone": "Europe/Moscow"
        }

    """

    def post(self, request):
        serializer = serializers.ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.data
        serializer.create(validated_data)

        return Response(data=validated_data, status=status.HTTP_200_OK)


class UpdateClientView(APIView):
    """
        API for update client

        Example of PUT method:
            {
            "phone": "79831575107",
            "code_of_mobile_operator": 983,
            "tag": "qwerty",
            "timezone": "Europe/Moscow"
            }

        """

    def put(self, request, client_id):
        serializer = serializers.ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        client = get_object_or_404(models.Client, id=client_id)
        serializer.update(instance=client, validated_data=validated_data)

        return Response(data=validated_data, status=status.HTTP_200_OK)
