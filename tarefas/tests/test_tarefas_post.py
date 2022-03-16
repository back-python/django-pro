import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp

def test_task_exist_db(resposta):
    assert Tarefa.objects.exists()

def test_redirect_after_saving_db(resposta):
    assert resposta.status_code == 302

@pytest.fixture
def response_invalid_item(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp

def test_task_invalid(response_invalid_item):
    assert not Tarefa.objects.exists()

def test_page_invalid_itens(response_invalid_item):
    assert response_invalid_item.status_code == 400