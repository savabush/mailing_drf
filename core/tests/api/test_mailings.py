from datetime import datetime
import pytz
from .fixtures import *


class TestStatusCodes:

    @pytest.mark.django_db
    def test_get_status_code_200_of_all_mailings(self, client, created_mailings):
        response = client.get('/api/v1/mailinglist/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_all_mailings(self, client):
        response = client.get('/api/v1/mailinglist/')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_create_mailing(self, client, data_of_mailing):
        response = client.post('/api/v1/mailinglist/', data=data_of_mailing, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_400_of_create_mailing(self, client):
        response = client.post('/api/v1/mailinglist/')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_get_status_code_200_of_get_mailing_by_id(self, client, id_of_mailing):
        response = client.get(f'/api/v1/mailinglist/{id_of_mailing}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_get_mailing_by_id(self, client):
        response = client.get('/api/v1/mailinglist/0')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_update_mailing(self, client, id_of_mailing, data_of_mailing):
        response = client.put(f'/api/v1/mailinglist/{id_of_mailing}', data=data_of_mailing, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_update_mailing(self, client):
        response = client.put(f'/api/v1/mailinglist/0')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_delete_mailing(self, client, id_of_mailing, data_of_mailing):
        response = client.delete(f'/api/v1/mailinglist/{id_of_mailing}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_delete_mailing(self, client):
        response = client.delete(f'/api/v1/mailinglist/0')
        assert response.status_code == 404


class TestResponsesData:

    @pytest.mark.django_db
    def test_create_mailing(self, client, data_of_mailing, format_of_time):
        response = client.post('/api/v1/mailinglist/', data=data_of_mailing, format='json')
        data = dict(response.data)
        assert data['datetime_of_start_mailing'] == \
               datetime.strptime(data_of_mailing['datetime_of_start_mailing'], format_of_time).replace(tzinfo=pytz.UTC)
        assert data['text'] == data_of_mailing['text']
        assert data['filters'] == data_of_mailing['filters']
        assert data['datetime_of_end_mailing'] == \
               datetime.strptime(data_of_mailing['datetime_of_end_mailing'], format_of_time).replace(tzinfo=pytz.UTC)

    @pytest.mark.django_db
    def test_len_after_create_mailings(self, client, created_mailings):
        response = client.get('/api/v1/mailinglist/')
        data = response.data
        assert len(data) == 2

    @pytest.mark.django_db
    def test_get_mailing_by_id(self, client, data_of_mailing, id_of_mailing):
        response = client.get(f'/api/v1/mailinglist/{id_of_mailing}')
        data = response.data
        assert data['datetime_of_start_mailing'] == data_of_mailing['datetime_of_start_mailing']
        assert data['text'] == data_of_mailing['text']
        assert data['filters'] == data_of_mailing['filters']
        assert data['datetime_of_end_mailing'] == data_of_mailing['datetime_of_end_mailing']

    @pytest.mark.django_db
    def test_update_mailing_by_id(self, client, data_of_mailing, id_of_mailing):
        response = client.put(f'/api/v1/mailinglist/{id_of_mailing}', data=data_of_mailing, format='json')
        data = response.data
        assert data['datetime_of_start_mailing'] == data_of_mailing['datetime_of_start_mailing']
        assert data['text'] == data_of_mailing['text']
        assert data['filters'] == data_of_mailing['filters']
        assert data['datetime_of_end_mailing'] == data_of_mailing['datetime_of_end_mailing']

    @pytest.mark.django_db
    def test_delete_mailing_by_id(self, client, id_of_mailing):
        response = client.delete(f'/api/v1/mailinglist/{id_of_mailing}')
        data = response.data
        assert data == {'message': 'success'}
