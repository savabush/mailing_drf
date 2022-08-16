from django.db.models.signals import post_save
from django.db.models import Q
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, get_list_or_404
from .tasks import send_message
from .models import Message, MailingList, Client
from .serializers import MessageSerializer
import pytz


@receiver(post_save, sender=MailingList, dispatch_uid='send_message_to_task_queue')
def send_message_to_task_queue(sender, instance, created, **kwargs):
    if created:
        tag = instance.filters.get('tag')
        code_of_mobile_operator = instance.filters.get('code_of_mobile_operator')

        clients = get_list_or_404(Client, Q(tag=tag) | Q(code_of_mobile_operator=code_of_mobile_operator))

        for client in clients:
            message_data = {
                'mailing': instance.id,
                'client': client.id
            }
            message_serializer = MessageSerializer(data=message_data)
            message_serializer.is_valid(raise_exception=True)
            validated_data_of_message = message_serializer.validated_data
            message_serializer.create(validated_data=validated_data_of_message)

            message = get_object_or_404(Message, mailing=instance.id, client=client.id)

            message_id = message.id
            phone = client.phone
            text = instance.text

            data = {
                'id': message_id,
                'phone': phone,
                'text': text
            }

            client_id = client.id
            mailing_id = instance.id

            timezone = pytz.timezone(client.timezone)
            send_message.apply_async(
                (data, mailing_id, client_id),
                eta=instance.datetime_of_start_mailing.replace(tzinfo=timezone).astimezone(pytz.UTC),
                expires=instance.datetime_of_end_mailing.replace(tzinfo=timezone).astimezone(pytz.UTC))
