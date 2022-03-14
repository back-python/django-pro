from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    """ Fixture usando URL nomeada do django (conferir arquivo URL.py) """
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_form_exist(resposta):
    assertContains(resposta,'<form')

def test_button_submit(resposta):
    assertContains(resposta, '<button type="submit"')