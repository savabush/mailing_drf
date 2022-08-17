from core.models import Client, MailingList
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def data_of_client():
    payload = {
        'phone': '79135005005',
        'tag': 'qweqwe',
        'timezone': 'Etc/GMT-7'
    }
    return payload


@pytest.fixture
def created_clients():
    payload_1 = {
        'phone': '79135005005',
        'tag': 'qweqwe',
        'timezone': 'Etc/GMT-7'
    }
    payload_2 = {
        'phone': '79835005004',
        'tag': 'qwest',
        'timezone': 'Europe/Moscow'
    }
    Client.objects.create(**payload_1)
    Client.objects.create(**payload_2)


@pytest.fixture
def format_of_time():
    return '%Y-%m-%dT%H:%M:%SZ'


@pytest.fixture
def data_of_mailing():
    payload = {
        "datetime_of_start_mailing": "2022-08-09T20:00:00Z",
        "text": "some text, which would be sent to clients",
        "filters": {"tag": "qwerty", "code_of_mobile_operator": "983"},
        "datetime_of_end_mailing": "2022-08-09T23:00:00Z"
    }
    return payload


@pytest.fixture
def created_mailings():
    payload_1 = {
        "datetime_of_start_mailing": "2022-08-09T20:00:00Z",
        "text": "some text, which would be sent to clients",
        "filters": {"tag": "qwerty", "code_of_mobile_operator": "983"},
        "datetime_of_end_mailing": "2022-08-09T23:00:00Z"
    }
    payload_2 = {
        "datetime_of_start_mailing": "2022-08-17T20:00:00Z",
        "text": "some text, which would be sent to clients",
        "filters": {"tag": "qwest", "code_of_mobile_operator": "913"},
        "datetime_of_end_mailing": "2022-12-20T23:00:00Z"
    }
    MailingList.objects.create(**payload_1)
    MailingList.objects.create(**payload_2)


@pytest.fixture
def id_of_client(created_clients):
    return Client.objects.all().first().id


@pytest.fixture
def id_of_mailing(created_mailings):
    return MailingList.objects.all().first().id
