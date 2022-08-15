from core import serializers, models
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from core.services.abstract_services import AbstractServices


class MailingListServices(AbstractServices):

    @staticmethod
    def _get_mailing_by_id(mailing_id):
        client = get_object_or_404(models.MailingList, id=mailing_id)
        return client

    @classmethod
    def validate_data_for_post_method(cls, serializer):
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        return validated_data

    @classmethod
    def validate_data_for_get_method_to_get_list(cls):
        mailing_list = get_list_or_404(models.MailingList)
        serializer = serializers.MailingListSerializer(mailing_list, many=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def validate_data_for_get_method_to_get_detail_info(cls, mailing_id, data):
        mailing_instance = get_object_or_404(models.MailingList, id=mailing_id)
        serializer = serializers.MailingListSerializer(mailing_instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def validate_data_for_put_method(cls, mailing_instance, data):
        serializer = serializers.MailingListSerializer(mailing_instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        return validated_data

    @classmethod
    def create(cls, validated_data, serializer):
        return serializer.create(validated_data)

    @classmethod
    def update(cls, mailing_id, data):
        mailing_instance = get_object_or_404(models.MailingList, id=mailing_id)
        for field, value in data.items():
            if hasattr(mailing_instance, field):
                setattr(mailing_instance, field, value)
            else:
                raise ValidationError('Invalid parameters')
        mailing_instance.save()
        return mailing_instance

    @classmethod
    def delete(cls, mailing_id):
        mailing_instance = get_object_or_404(models.MailingList, id=mailing_id)
        mailing_instance.delete()

    @classmethod
    def searching_by_filters(cls, tag, code_of_mobile_operator):
        queryset = models.MailingList.objects.filter(
            Q(filters__tag=tag) | Q(filters__code_of_mobile_operator=code_of_mobile_operator)
        )
        return queryset

    @classmethod
    def get_queryset_of_messages_by_mailing_id(cls, mailing_id):
        mailing = cls._get_mailing_by_id(mailing_id=mailing_id)
        return mailing.mailing.all()

    @classmethod
    def to_send(cls, mailing_instance):
        now = timezone.now()
        return mailing_instance.datetime_of_start_mailing <= now <= mailing_instance.datetime_of_end_mailing
