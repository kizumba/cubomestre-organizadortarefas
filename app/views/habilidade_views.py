from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import Habilidade

class HabilidadeListView(LoginRequiredMixin, ListView):
    model = Habilidade
    fields = "__all__"
    template_name = "habilidades/lista_habilidades.html"

class HabilidadeCreateView(CreateView):
    model = Habilidade
    fields = "__all__"
    template_name = "habilidades/form_habilidade.html"
    success_url = "lista_habilidades"

class HabilidadeUpdateView(LoginRequiredMixin, UpdateView):
    model = Habilidade
    fields = "__all__"
    template_name = "habilidades/form_habilidade.html"
    success_url = reverse_lazy("lista_habilidades")

class HabilidadeDeleteView(LoginRequiredMixin, DeleteView):
    model = Habilidade
    template_name = "habilidades/apagar_habilidade.html"
    success_url = reverse_lazy("lista_habilidades")
