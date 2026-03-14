from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from app.models import Funcionario, FuncionarioHabilidade, Habilidade
from app.forms.funcionario_forms import (
    FuncionarioForm,
    EnderecoForm,
    FuncionarioChangeForm
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
        context["habilidades"] = Habilidade.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        funcionario_form = FuncionarioForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if funcionario_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.endereco = endereco
            funcionario.save()
            
            habilidades_selecionadas = request.POST.getlist('habilidades')
            FuncionarioHabilidade.objects.filter(colaborador=funcionario).delete()
            for habilidade_id in habilidades_selecionadas:
                FuncionarioHabilidade.objects.create(
                    colaborador=funcionario,
                    habilidade_id=habilidade_id
                )

        return HttpResponseRedirect(reverse("lista_funcionarios"))

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "funcionarios/detalhes_funcionario.html"

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    form_class = FuncionarioChangeForm
    template_name = "funcionarios/form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

    def get_context_data(self, **kwargs):
        context = super(FuncionarioUpdateView, self).get_context_data(**kwargs)
        context["form"] = FuncionarioChangeForm(instance=self.object)
        context["endereco_form"] = EnderecoForm(instance=self.object.endereco)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        funcionario = self.object
        funcionario_form = FuncionarioChangeForm(data=request.POST or None, instance=funcionario)
        endereco_form = EnderecoForm(data=request.POST or None, instance=funcionario.endereco)
        if funcionario_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.endereco = endereco
            funcionario.save()

            habilidades_selecionadas = request.POST.getlist('habilidades')
            FuncionarioHabilidade.objects.filter(colaborador=funcionario).delete()
            for habilidade_id in habilidades_selecionadas:
                FuncionarioHabilidade.objects.create(
                    colaborador=funcionario,
                    habilidade_id=habilidade_id
                )

            return HttpResponseRedirect(reverse("lista_funcionarios"))
        else:
            # Se os formulários forem inválidos, renderiza o template novamente com os erros
            context = self.get_context_data(**kwargs)
            context["form"] = funcionario_form
            context["endereco_form"] = endereco_form
            return self.render_to_response(context)

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "funcionarios/apagar_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

    def post(self, request, *args, **kwargs):
        funcionario = Funcionario.objects.get(id=kwargs["pk"])
        funcionario.endereco.delete()
        funcionario.delete()
        return HttpResponseRedirect(reverse("lista_funcionarios"))