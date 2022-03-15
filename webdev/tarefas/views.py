from django.urls.base import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from webdev.tarefas.forms import TarefaForm, TarefaNovaForm
from webdev.tarefas.models import Tarefa

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(concluida=False).all()
            return render(request, 'tarefas/home.html', {'form':form, 'tarefas_pendentes':tarefas_pendentes}, status=400)
    
    tarefas_pendentes = Tarefa.objects.filter(concluida=False).all()
    return render(request, 'tarefas/home.html', {'tarefas_pendentes':tarefas_pendentes})

def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST, instance=tarefa)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))