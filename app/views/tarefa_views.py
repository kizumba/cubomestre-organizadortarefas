from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from app.models import Tarefa
from app.forms.tarefa_forms import TarefaForm

class TarefaListView(ListView):
    model = Tarefa
    fields = "__all__"
    template_name = "tarefas/lista_tarefas.html"

class TarefaCreateView(CreateView):
    model = Tarefa
    # fields = "__all__"
    form_class = TarefaForm
    template_name = "tarefas/form_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")


class TarefaUpdateView(UpdateView):
    model = Tarefa
    # fields = "__all__"
    form_class = TarefaForm
    template_name = "tarefas/form_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")


class TarefaDetailView(DetailView):
    model = Tarefa
    template_name = "tarefas/detalhes_tarefa.html"

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = "tarefas/apagar_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")