from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from app.models import Tarefa
from app.forms.tarefa_forms import TarefaForm

class TarefaListView(LoginRequiredMixin, ListView):
    model = Tarefa
    fields = "__all__"
    template_name = "tarefas/lista_tarefas.html"

class TarefaCreateView(UserPassesTestMixin, CreateView):
    model = Tarefa
    # fields = "__all__"
    form_class = TarefaForm
    template_name = "tarefas/form_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")

    def test_func(self):
        return self.request.user.cargo == 1 or self.request.user.cargo == 3


class TarefaUpdateView(UserPassesTestMixin, UpdateView):
    model = Tarefa
    # fields = "__all__"
    form_class = TarefaForm
    template_name = "tarefas/form_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")

    def test_func(self):
        return self.request.user.cargo == 1 or self.request.user.cargo == 3


class TarefaDetailView(LoginRequiredMixin, DetailView):
    model = Tarefa
    template_name = "tarefas/detalhes_tarefa.html"

class TarefaDeleteView(UserPassesTestMixin, DeleteView):
    model = Tarefa
    template_name = "tarefas/apagar_tarefa.html"
    success_url = reverse_lazy("lista_tarefas")

    def test_func(self):
        return self.request.user.cargo == 1
        