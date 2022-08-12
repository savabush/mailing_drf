from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import serializers, models


class GetClientsOrCreateClientView(APIView):
    """
    API for get all clients with or without filters or add client to DB by serializer

    Example of url to GET method:

        url = api/v1/clients/?tag=qwerty

    Example of POST method:
        {
        "phone": "79831575107",
        "code_of_mobile_operator": 983,
        "tag": "qwerty",
        "timezone": "Europe/Moscow"
        }

    """

    def get(self, request):
        query_params = {field: value for field, value in request.query_params.items()}
        list_of_clients = get_list_or_404(models.Client, **query_params)
        serializer = serializers.ClientSerializer(list_of_clients, many=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.data
        serializer.create(validated_data)

        return Response(data=validated_data, status=status.HTTP_200_OK)


class UpdateOrDeleteClientView(APIView):
    """
        API for get, update or delete client

        Example of PUT method:
            {
            "phone": "79831575107",
            "code_of_mobile_operator": 983,
            "tag": "qwerty",
            "timezone": "Europe/Moscow"
            }

            OR

            {
            "tag": "qwerty"
            }

        """

    def get(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)

        serializer = serializers.ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def put(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)
        data = request.data
        for field, value in data.items():
            if hasattr(client, field):
                setattr(client, field, value)
            else:
                raise ValidationError('Invalid parameters')
        client.save()

        serializer = serializers.ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def delete(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)
        client.delete()
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)


class GetMailingListOrCreateMailing(APIView):
    """
    API for get mailing list and count of sent messages with grouping by status
    or add mailing to DB

    Example of POST method:
        {
        "datetime_of_start_mailing": "2022-08-09 20:00:00",
        "text": "some text, which would be sent to clients",
        "filters": {"tag": "qwerty", "code_of_mobile_operator": "983"},
        "datetime_of_end_mailing": "2022-08-09 23:00:00"
        }

    """

    def get(self, request):
        mailing_list = get_list_or_404(models.MailingList)
        serializer = serializers.MailingListSerializer(mailing_list, many=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.MailingListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.data
        serializer.create(validated_data)

        return Response(data=validated_data, status=status.HTTP_200_OK)


class UpdateOrDeleteMailingListView(APIView):
    """
        API for get, update or delete client

        Example of PUT method:
            {
            "phone": "79831575107",
            "code_of_mobile_operator": 983,
            "tag": "qwerty",
            "timezone": "Europe/Moscow"
            }

            OR

            {
            "tag": "qwerty"
            }

        """

    def get(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)

        serializer = serializers.ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def put(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)
        data = request.data
        for field, value in data.items():
            if hasattr(client, field):
                setattr(client, field, value)
            else:
                raise ValidationError('Invalid parameters')
        client.save()

        serializer = serializers.ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        return Response(data=validated_data, status=status.HTTP_200_OK)

    def delete(self, request, client_id):
        client = get_object_or_404(models.Client, id=client_id)
        client.delete()
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)
