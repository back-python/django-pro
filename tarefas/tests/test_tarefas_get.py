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
        Tarefa(nome='Tarefa 01', concluida=False),
        Tarefa(nome='Tarefa 02', concluida=False),
    ]

    Tarefa.objects.bulk_create(tarefas)

    return tarefas

@pytest.fixture
def response_with_to_do_list(client, list_pending_tasks, list_completed_tasks):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_list_pending_tasks_exists(response_with_to_do_list, list_pending_tasks):
    for tarefa in list_pending_tasks:
        assertContains(response_with_to_do_list, tarefa.nome)

@pytest.fixture
def list_completed_tasks(db):
    tarefas = [
        Tarefa(nome='Tarefa 03', concluida=True),
        Tarefa(nome='Tarefa 04', concluida=True),
    ]

    Tarefa.objects.bulk_create(tarefas)

    return tarefas

def test_list_completed_tasks_exists(response_with_to_do_list, list_completed_tasks):
    for tarefa in list_completed_tasks:
        assertContains(response_with_to_do_list, tarefa.nome)
