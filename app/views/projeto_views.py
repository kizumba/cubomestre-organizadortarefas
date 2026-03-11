from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from app.models import Projeto

class ProjetoListView(ListView):
    model = Projeto
    fields = "__all__"
    template_name = "projetos/lista_projetos.html"

class ProjetoCreateView(CreateView):
    model = Projeto
    fields = "__all__"
    template_name = "projetos/form_projeto.html"
    success_url = "lista_projetos"

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = "__all__"
    template_name = "projetos/form_projeto.html"
    success_url = reverse_lazy("lista_projetos")

class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = "projetos/apagar_projeto.html"
    success_url = reverse_lazy("lista_projetos")