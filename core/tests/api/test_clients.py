from .fixtures import *


class TestStatusCodes:

    @pytest.mark.django_db
    def test_get_status_code_200_of_all_clients(self, client, created_clients):
        response = client.get('/api/v1/clients/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_all_clients(self, client):
        response = client.get('/api/v1/clients/')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_create_client(self, client, data_of_client):
        response = client.post('/api/v1/clients/', data=data_of_client)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_400_of_create_client(self, client):
        response = client.post('/api/v1/clients/')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_get_status_code_200_of_get_client_by_id(self, client, id_of_client):
        response = client.get(f'/api/v1/clients/{id_of_client}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_get_client_by_id(self, client):
        response = client.get('/api/v1/clients/0')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_update_client(self, client, id_of_client, data_of_client):
        response = client.put(f'/api/v1/clients/{id_of_client}', data=data_of_client)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_update_client(self, client):
        response = client.put(f'/api/v1/clients/0')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_delete_client(self, client, id_of_client, data_of_client):
        response = client.delete(f'/api/v1/clients/{id_of_client}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_delete_client(self, client):
        response = client.delete(f'/api/v1/clients/0')
        assert response.status_code == 404


class TestResponsesData:

    @pytest.mark.django_db
    def test_create_client(self, client, data_of_client):
        response = client.post('/api/v1/clients/', data=data_of_client)
        data = response.data
        assert data == data_of_client

    @pytest.mark.django_db
    def test_len_after_create_clients(self, client, created_clients):
        response = client.get('/api/v1/clients/')
        data = response.data
        assert len(data) == 2

    @pytest.mark.django_db
    def test_get_client_by_id(self, client, data_of_client, id_of_client):
        response = client.get(f'/api/v1/clients/{id_of_client}')
        data = response.data
        assert data['phone'] == data_of_client['phone']
        assert data['code_of_mobile_operator'] == data_of_client['phone'][1:4]
        assert data['timezone'] == data_of_client['timezone']
        assert data['tag'] == data_of_client['tag']

    @pytest.mark.django_db
    def test_update_client_by_id(self, client, data_of_client, id_of_client):
        response = client.put(f'/api/v1/clients/{id_of_client}', data=data_of_client)
        data = response.data
        assert data['phone'] == data_of_client['phone']
        assert data['code_of_mobile_operator'] == data_of_client['phone'][1:4]
        assert data['timezone'] == data_of_client['timezone']
        assert data['tag'] == data_of_client['tag']

    @pytest.mark.django_db
    def test_delete_client_by_id(self, client, id_of_client):
        response = client.delete(f'/api/v1/clients/{id_of_client}')
        data = response.data
        assert data == {'message': 'success'}
