from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from app.models import TipoFuncionario

class TipoFuncionarioListView(ListView):
    model = TipoFuncionario
    template_name = "tipo_funcionarios/lista_tipo_funcionarios.html"

class TipoFuncionarioCreateView(CreateView):
    model = TipoFuncionario
    fields = "__all__"
    template_name = "tipo_funcionarios/form_tipo_funcionario.html"
    success_url = "lista_tipo_funcionarios"

class TipoFuncionarioUpdateView(UpdateView):
    model = TipoFuncionario
    fields = "__all__"
    template_name = "tipo_funcionarios/form_tipo_funcionario.html"
    success_url = reverse_lazy("lista_tipo_funcionarios")

class TipoFuncionarioDeleteView(DeleteView):
    model = TipoFuncionario
    template_name = "tipo_funcionarios/tipo_funcionario_confirm_delete.html"
    success_url = reverse_lazy("lista_tipo_funcionarios")