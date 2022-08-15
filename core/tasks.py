import os
import requests
import pytz
import datetime
from celery.utils.log import get_task_logger

from .models import Message, Client, MailingList
from mailing.celery import app

logger = get_task_logger(__name__)


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, client_id, mailing_id):
    token = os.getenv('TOKEN_OF_SERVICE')
    url = os.getenv('URL_OF_SERVICE')
    mailing = MailingList.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)

    if mailing.datetime_of_start_mailing <= now <= mailing.datetime_of_end_mailing:
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
        time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                     int(mailing.datetime_of_start_mailing.strftime('%H:%M:%S')[:2]))
        logger.info(f"Message id: {data['id']}, "
                    f"The current time is not for sending the message,"
                    f"restarting task after {60 * 60 * time} seconds")
        return self.retry(countdown=60 * 60 * time)
