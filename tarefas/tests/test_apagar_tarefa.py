import pytest
from webdev.tarefas.models import Tarefa
from django.urls import reverse

@pytest.fixture
def task(db):
    return Tarefa.objects.create(nome='Tarefa 01', concluida=False)

@pytest.fixture
def response(client, task):
    resp = client.post(
        reverse('tarefas:apagar', kwargs={'tarefa_id':task.id}),
    )
    return resp

def test_delete_task(response):
    assert not Tarefa.objects.exists()