from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = '__all__'


class MessageCountSerializer(serializers.ModelSerializer):
    count_of_sent = serializers.SerializerMethodField()

    class Meta:
        model = models.Message
        fields = ['count_of_sent', 'status']

    def get_count_of_sent(self, obj):
        queryset = self.Meta.model.objects
        queryset_of_sent_messages = queryset.filter(status=True, mailing_id=obj.mailing_id)
        return len(queryset_of_sent_messages)


class MailingListSerializer(serializers.ModelSerializer):
    detail_info = MessageCountSerializer(read_only=True, source='mailing')

    class Meta:
        model = models.MailingList
        fields = [
            'datetime_of_start_mailing',
            'text',
            'filters',
            'datetime_of_end_mailing',
            'detail_info'
        ]
