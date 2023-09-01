from django.test import Client


def test_if_request_to_admin_page_returns_301_http_status_code(client: Client):
    response = client.get('/admin')
    assert response.status_code == 301
