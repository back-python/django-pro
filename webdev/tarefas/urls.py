from webdev.tarefas import views
from django.urls import path


app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),
    path('apagar/<int:tarefa_id>', views.apagar, name='apagar'),
]