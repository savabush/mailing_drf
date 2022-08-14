from core import serializers, models
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from core.services.abstract_services import AbstractServices


class ClientServices(AbstractServices):

    @staticmethod
    def _get_client_by_id(client_id):
        client = get_object_or_404(models.Client, id=client_id)
        return client

    @classmethod
    def validate_data_for_post_method(cls, serializer):
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def validate_data_for_get_method_to_get_list(cls, query_params: dict):
        list_of_clients = get_list_or_404(models.Client, **query_params)
        serializer = serializers.ClientSerializer(list_of_clients, many=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def validate_data_to_get_detail_info(cls, client_id, data):
        client = cls._get_client_by_id(client_id=client_id)
        serializer = serializers.ClientSerializer(client, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def validate_data_for_put_method(cls, client_instance, data):
        serializer = serializers.ClientSerializer(client_instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def create(cls, validated_data, serializer):
        return serializer.create(validated_data)

    @classmethod
    def update(cls, client_id, data):
        client = cls._get_client_by_id(client_id=client_id)
        for field, value in data.items():
            if hasattr(client, field):
                setattr(client, field, value)
            else:
                raise ValidationError('Invalid parameters')
        client.save()
        return client

    @classmethod
    def delete(cls, client_id):
        client = cls._get_client_by_id(client_id=client_id)
        client.delete()

    @classmethod
    def get_queryset_of_messages_by_client_id(cls, client_id):
        client = cls._get_client_by_id(client_id=client_id)
        return client.client.all()

    @classmethod
    def searching_by_filters(cls, tag, code_of_mobile_operator):
        queryset = models.Client.objects.filter(
            Q(tag=tag) | Q(code_of_mobile_operator=code_of_mobile_operator)
        )
        return queryset
