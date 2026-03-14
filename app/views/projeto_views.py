from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from app.models import Projeto, Funcionario

from app.forms.projeto_forms import ProjetoForm

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    fields = "__all__"
    template_name = "projetos/lista_projetos.html"

class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    # fields = ("nome", "status","descricao","custo", "data_entrega_prevista", "data_entrega_real", "cliente","gerente",)
    form_class = ProjetoForm
    template_name = "projetos/form_projeto.html"
    success_url = reverse_lazy("lista_projetos")

    def get_inicital(self):
        initial = super().get_initial()

        gerente_pk = self.kwargs.get("gerente_pk")
        if gerente_pk:
            try:
                gerente = Funcionario.objects.get(pk=gerente_pk)
                initial['gerente_nome'] = gerente.username
                initial['gerente_id'] = gerente_pk
            except Funcionario.DoesNotExist:
                pass
        return initial
    
    def get_contect_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gerente_pk'] = self.kwargs.get("gerente_k")

        if context["gerente_pk"]:
            try:
                context["gerente"] = Funcionario.objects.get(pk=context["gerente_pk"])
            except Funcionario.DoesNotExist:
                pass
        return context

    def form_valid(self, form):
        gerente_pk = self.kwargs.get("gerente_pk")
        if gerente_pk:
            form.instance.gerente_id = gerente_pk
        return super().form_valid(form)

class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    # fields = "__all__"
    form_class = ProjetoForm
    template_name = "projetos/form_projeto.html"
    success_url = reverse_lazy("lista_projetos")

class ProjetoDetailView(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = "projetos/detalhes_projeto.html"

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    template_name = "projetos/apagar_projeto.html"
    success_url = reverse_lazy("lista_projetos")