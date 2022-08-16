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
            'id',
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
