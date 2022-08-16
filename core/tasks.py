import os
import requests
import pytz
import datetime
from django.shortcuts import get_object_or_404
from celery.utils.log import get_task_logger

from .models import Message, Client, MailingList
from mailing.celery import app

logger = get_task_logger(__name__)


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, mailing_id, client_id):
    token = os.getenv('TOKEN_OF_SERVICE')
    url = os.getenv('URL_OF_SERVICE')
    mailing = get_object_or_404(MailingList, id=mailing_id)
    client = get_object_or_404(Client, id=client_id)

    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone).astimezone(pytz.UTC)
    start_mailing = mailing.datetime_of_start_mailing.replace(tzinfo=timezone).astimezone(pytz.UTC)
    end_mailing = mailing.datetime_of_end_mailing.replace(tzinfo=timezone).astimezone(pytz.UTC)

    if start_mailing <= now <= end_mailing:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f"Message if: {data['id']} is error")
            raise self.retry(exc=exc)
        else:
            logger.info(f"Message id: {data['id']}, Sending status: 'Sent'")
            Message.objects.filter(pk=data['id']).update(status=True)
    else:
        time = (start_mailing - now).seconds
        logger.info(f"Message id: {data['id']}, "
                    f"The current time is not for sending the message,"
                    f"restarting task after {time + 1} seconds")
        return self.retry(countdown=time + 1)
