from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from .services.clients import ClientServices
from .services.mailing_list import MailingListServices


class GetClientsOrCreateClientView(APIView):
    """
    API for get all clients with or without filters or add client to DB by serializer

    Example of url to GET method:

        url = api/v1/clients/?tag=qwerty

    Example of POST method:
        {
        "phone": "79831575107",
        "tag": "qwerty",
        "timezone": "Europe/Moscow"
        }

    """

    def get(self, request):
        query_params = {field: value for field, value in request.query_params.items()}
        validated_data = ClientServices.validate_data_for_get_method_to_get_list(query_params=query_params)
        return Response(data=validated_data, status=status.HTTP_200_OK)

    def post(self, request):
        client_serializer = serializers.ClientSerializer(data=request.data)
        validated_data_of_client = ClientServices.validate_data_for_post_method(serializer=client_serializer)
        ClientServices.create(validated_data=validated_data_of_client, serializer=client_serializer)
        return Response(data=validated_data_of_client, status=status.HTTP_200_OK)


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
        validated_data = ClientServices.validate_data_to_get_detail_info(
            client_id=client_id,
            data=request.data
        )
        return Response(data=validated_data, status=status.HTTP_200_OK)

    def put(self, request, client_id):
        data = request.data
        client = ClientServices.update(client_id=client_id, data=data)
        validated_data_of_client = ClientServices.validate_data_for_put_method(
            client_instance=client,
            data=data
        )
        return Response(data=validated_data_of_client, status=status.HTTP_200_OK)

    def delete(self, request, client_id):
        ClientServices.delete(client_id=client_id)
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
        validated_data = MailingListServices.validate_data_for_get_method_to_get_list()
        return Response(data=validated_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.MailingListSerializer(data=request.data)
        validated_data_of_mailing = MailingListServices.validate_data_for_post_method(serializer=serializer)
        MailingListServices.create(validated_data=validated_data_of_mailing, serializer=serializer)
        return Response(data=validated_data_of_mailing, status=status.HTTP_200_OK)


class UpdateOrDeleteMailingListView(APIView):
    """
        API for get, update or delete mailing

        Example of PUT method:
            {
            "datetime_of_start_mailing": "2022-08-09T20:00:00Z",
            "text": "some text, which would be sent to clients",
            "filters": {
                "tag": "qwerty",
                "code_of_mobile_operator": "983"
            },
            "datetime_of_end_mailing": "2022-08-09T23:00:00Z",
            }

            OR

            {
            "text": "some text, which would be sent to clients",
            "filters": {
                "tag": "qwerty",
                "code_of_mobile_operator": "983"
            }
            }

        """

    def get(self, request, mailing_id):
        validated_data = MailingListServices.validate_data_for_get_method_to_get_detail_info(
            mailing_id=mailing_id,
            data=request.data
        )
        return Response(data=validated_data, status=status.HTTP_200_OK)

    def put(self, request, mailing_id):
        data = request.data
        mailing_instance = MailingListServices.update(mailing_id=mailing_id, data=data)
        validated_data_of_mailing = MailingListServices.validate_data_for_put_method(
            mailing_instance=mailing_instance,
            data=data
        )
        return Response(data=validated_data_of_mailing, status=status.HTTP_200_OK)

    def delete(self, request, mailing_id):
        MailingListServices.delete(mailing_id=mailing_id)
        return Response(data={'message': 'success'}, status=status.HTTP_200_OK)
