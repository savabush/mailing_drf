from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .tasks import send_message
from .models import Message, MailingList, Client
from .services.mailing_list import MailingListServices


@receiver(post_save, sender=Message, dispatch_uid='send_message_to_task_queue')
def send_message_to_task_queue(sender, instance, created, **kwargs):
    if created:
        mailing_instance = get_object_or_404(MailingList, id=instance.mailing.id)
        client_instance = get_object_or_404(Client, id=instance.client.id)

        message_id = instance.id
        phone = client_instance.phone
        text = mailing_instance.text

        data = {
            'id': message_id,
            'phone': phone,
            'text': text
        }

        client_id = client_instance.id
        mailing_id = mailing_instance.id

        if MailingListServices.to_send(mailing_instance=mailing_instance):
            send_message.apply_async(
                (data, client_id, mailing_id),
                expires=mailing_instance.datetime_of_end_mailing)
        else:
            send_message.apply_async(
                (data, client_id, mailing_id),
                eta=mailing_instance.datetime_of_start_mailing,
                expires=mailing_instance.datetime_of_end_mailing)
