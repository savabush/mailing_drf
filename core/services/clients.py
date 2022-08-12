from core import serializers, models
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.exceptions import ValidationError

class ClientServices:

    @classmethod
    def validate_data_for_post_method(cls, data):
        serializer = serializers.ClientSerializer(data=data)
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
    def validate_data_for_get_method_to_get_detail_info(cls, client_id, data):
        client = get_object_or_404(models.Client, id=client_id)
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
    def create(cls, validated_data):
        serializers.create(validated_data)

    @classmethod
    def update(cls, client_id, data):
        client = get_object_or_404(models.Client, id=client_id)
        for field, value in data.items():
            if hasattr(client, field):
                setattr(client, field, value)
            else:
                raise ValidationError('Invalid parameters')
        client.save()
        return client

    @classmethod
    def delete(cls, client_id):
        client = get_object_or_404(models.Client, id=client_id)
        client.delete()
