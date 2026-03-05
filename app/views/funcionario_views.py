from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from app.models import Funcionario
from app.forms.funcionario_forms import (
    FuncionarioForm,
    EnderecoForm,
    ContatoForm,
)

class FuncionarioListView(ListView):
    model = Funcionario
    fields = "__all__"
    template_name = "funcionarios/lista_funcionarios.html"

class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = "funcionarios/form_funcionario.html"
    success_url = "lista_funcionarios"

    def get_context_data(self, **kwargs):
        context = super(FuncionarioCreateView, self).get_context_data(**kwargs)
        context['form'] = FuncionarioForm()
        context["endereco_form"] = EnderecoForm()
        context["contato_form"] = ContatoForm()
        return context

    def post(self, request, *args, **kwargs):
        funcionario_form = FuncionarioForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        contato_form = ContatoForm(data=request.POST)
        if funcionario_form.is_valid() and endereco_form.is_valid() and contato_form.is_valid():
            endereco = endereco_form.save()
            contato = contato_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.endereco = endereco
            funcionario.contato = contato
            funcionario.save()

        return HttpResponseRedirect(reverse("lista_funcionarios"))

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "funcionarios/detalhes_funcionario.html"
