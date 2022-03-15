import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    """ Fixture usando URL nomeada do django (conferir arquivo URL.py) """
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_form_exist(resposta):
    assertContains(resposta,'<form')

def test_button_submit(resposta):
    assertContains(resposta, '<button type="submit"')

@pytest.fixture
def list_pending_tasks(db):
    tarefas = [
        Tarefa('1', concluida=False),
        Tarefa('2', concluida=False),
    ]

    Tarefa.objects.bulk_create(tarefas)

    return tarefas

@pytest.fixture
def response_with_to_do_list(client, list_pending_tasks):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_list_pending_tasks_exists(response_with_to_do_list, list_pending_tasks):
    for tarefa in list_pending_tasks:
        assertContains(response_with_to_do_list, tarefa.nome)
