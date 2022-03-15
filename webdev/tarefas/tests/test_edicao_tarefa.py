import pytest
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa
from django.urls import reverse

@pytest.fixture
def pending_task(db):
    return Tarefa.objects.create(nome='Tarefa 01', concluida=False)

@pytest.fixture
def response_with_pending_task(client, pending_task):
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id':pending_task.id}),
        data={'concluida':'true', 'nome':f'{pending_task.nome}-edited'} 
    )
    return resp

def test_status_code(response_with_pending_task):
    assert response_with_pending_task.status_code == 302

def test_completed_task(response_with_pending_task):
    assert Tarefa.objects.first().concluida
