from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from app.models import Habilidade

class HabilidadeListView(ListView):
    model = Habilidade
    fields = "__all__"
    template_name = "habilidades/lista_habilidades.html"

class HabilidadeCreateView(CreateView):
    model = Habilidade
    fields = "__all__"
    template_name = "habilidades/form_habilidade.html"
    success_url = "lista_habilidades"