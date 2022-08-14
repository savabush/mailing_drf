from django.shortcuts import get_object_or_404
from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = '__all__'


class MailingListSerializer(serializers.ModelSerializer):
    count_of_sent = serializers.SerializerMethodField(read_only=True)
    count_of_unsent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.MailingList
        fields = [
            'datetime_of_start_mailing',
            'text',
            'filters',
            'datetime_of_end_mailing',
            'count_of_sent',
            'count_of_unsent'
        ]

    def get_count_of_sent(self, obj):
        return len(obj.mailing.filter(status=True))

    def get_count_of_unsent(self, obj):
        return len(obj.mailing.filter(status=False))


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = '__all__'

    def create(self, validated_data):
        client_id = validated_data['client']
        client = get_object_or_404(models.Client, id=client_id)
        mailing_id = validated_data['mailing']
        mailing = get_object_or_404(models.MailingList, id=mailing_id)
        new_validated_data = {
            'client': client,
            'mailing': mailing
        }
        return super().create(validated_data=new_validated_data)
