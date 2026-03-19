from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from app.models import Funcionario, Projeto, Tarefa, Habilidade

class GerenteDashboard(View):
    template_name = "gerentes/dashboard_gerente.html"

    def get(self, request, *args, **kwargs):
        context = {}

        gerente = Funcionario.objects.get(pk=kwargs["pk"])
        projetos = Projeto.objects.filter(gerente=gerente)
        funcionarios = Funcionario.objects.all()
        tarefas = Tarefa.objects.all()
        habilidades = Habilidade.objects.all()

        context.update({
            "projetos":projetos,
            "funcionarios":funcionarios,
            "tarefas":tarefas,
            "habilidades":habilidades,
            "gerente":gerente
            })

        return render(request, self.template_name, context)