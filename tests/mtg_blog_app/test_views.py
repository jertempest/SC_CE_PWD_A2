from django.test import TestCase
from django.urls import reverse

# def test_index():
#     assert False

def test_index_ok(client):
    response = client.get('/')
    assert response.status_code == 200